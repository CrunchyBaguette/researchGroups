from __future__ import annotations

from typing import Sequence
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
        self,
        sender: str,
        recipient: str,
        subject: str,
        message: str,
    ) -> None:
        self.message = EmailMultiAlternatives(subject=subject, body=message, to=[recipient], from_email=sender)
        self.message.mixed_subtype = "related"

    def send(self) -> int:
        return self.message.send()


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
