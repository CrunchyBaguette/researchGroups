from __future__ import annotations

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Literal, Sequence
from dataclasses import dataclass
from collections.abc import Mapping


class EmailBuilder:
    def __init__(
        self, sender: str, subtype: Literal["alternative", "mixed"] = "mixed"
    ) -> None:
        self.sender = sender
        self.message = MIMEMultipart(subtype)
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

    def build_django_mail(self) -> EmailDjango:
        subject = self.message["Subject"]
        sender = self.message["From"]
        receivers = self.receivers
        html = ""
        message = ""

        for p in self.message.get_payload():
            if p.get_content_type == "text/plain":
                message = p.get_payload()
            elif p.get_content_type == "text/html":
                html = p.get_payload()

        return EmailDjango(
            subject=subject,
            message=message,
            from_email=sender,
            recipient_list=receivers,
            html_message=html,
        )


@dataclass
class Email(Mapping):
    from_addr: str
    to_addr: str | Sequence[str]
    msg: bytes | str

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]


@dataclass
class EmailDjango(Mapping):
    subject: str
    message: str
    from_email: str
    recipient_list: list[str]
    html_message: str
    fail_silently: bool = False

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]
