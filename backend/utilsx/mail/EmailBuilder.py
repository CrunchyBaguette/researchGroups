from __future__ import annotations

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Literal, Sequence
from dataclasses import dataclass
from collections.abc import Mapping
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.core.mail.backends.base import BaseEmailBackend


def send_messages_conn(messages: list[EmailMessage], connection: BaseEmailBackend):
    connection.open()
    sent = 0
    for m in messages:
        m.connection = connection
        sent += m.send()

    connection.close()
    return sent


class EmailBuilder:
    def __init__(
        self, sender: str, subtype: Literal["alternative", "mixed"] = "mixed"
    ) -> None:
        self.sender = sender
        self.message = MIMEMultipart(subtype)
        self.message["From"] = sender
        self.receivers: list[str] = []

    def add_text(self, text: str) -> EmailBuilder:
        text_msg = MIMEText(text, "plain")
        self.message.attach(text_msg)
        return self

    def add_html(self, html: str) -> EmailBuilder:
        text_html = MIMEText(html, "html")
        self.message.attach(text_html)
        return self

    def set_sender(self, sender: str) -> EmailBuilder:
        self.sender = sender
        self.message["From"] = self.sender
        return self

    def add_receiver(self, receiver: str) -> EmailBuilder:
        self.receivers.append(receiver)
        return self

    def build(self) -> Email:
        return Email(self.sender, self.receivers, self.message.as_string())

    def add_subject(self, subject: str):
        self.message["Subject"] = subject
        return self

    def build_django_mail(self) -> EmailMultiAlternatives:
        subject = self.message["Subject"]
        sender = self.message["From"]
        receivers = self.receivers
        html = None
        message = None

        for p in self.message.get_payload():
            if p.get_content_type() == "text/plain":
                message = p.get_payload()
            elif p.get_content_type() == "text/html":
                html = p.get_payload()

        email = EmailMultiAlternatives(
            subject=subject, from_email=sender, to=receivers, body=message
        )
        if html is not None:
            email.attach_alternative(html, "text/html")

        return email

    def send(self, connection=None) -> int:
        email = self.build_django_mail()
        if connection:
            email.connection = connection
            connection.open()
            sent: int = email.send()
            connection.close()
            return sent
        else:
            return email.send()


@dataclass
class Email(Mapping):
    """
    Simple wrapper for email to send using smtplib.send()

    You can use it like that

    :Example:

    >>> import smtplib, ssl
    >>> context = smtplib.ssl.create_default_context()
    >>> with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    >>>    server.login("sender_email", "password")
    >>>    server.sendmail(**Email)

    .. note:: Preffer to use Django EmailMultiAlternatives
    """

    from_addr: str
    to_addr: str | Sequence[str]
    msg: bytes | str

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]
