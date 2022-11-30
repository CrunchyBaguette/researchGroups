import pytest
from django.core import mail

from ..EmailBuilder import EmailBuilder


@pytest.mark.order(1)
def test_send_simple_mail(mailoutbox):
    email = (
        EmailBuilder("sender@example.com")
        .add_receiver("receiver@example.com")
        .add_text("This is a simple text")
        .add_subject("Test subject")
        .build_django_mail()
    )

    email.send()
    received = mailoutbox[0]

    assert len(mailoutbox) == 1, "Inbox is not empty"
    assert received.subject == "Test subject"
    assert received.body == "This is a simple text"
    assert received.from_email == "sender@example.com"
    assert received.to == ["receiver@example.com"]


@pytest.mark.order(2)
def test_send_html(mailoutbox):
    html = '<p style="color:blue;font-size:46px;">I\'m a big, blue, <strong>strong</strong> paragraph</p>'
    email = (
        EmailBuilder("sender@example.com")
        .add_receiver("receiver@example.com")
        .add_text("This is a simple text")
        .add_subject("Test subject")
        .add_html(html)
        .build_django_mail()
    )

    email.send()
    received = mailoutbox[0]

    assert len(mailoutbox) == 1, "Inbox is not empty"
    assert received.alternatives[0][1] == "text/html"
    assert (
        received.alternatives[0][0]
        == '<p style="color:blue;font-size:46px;">I\'m a big, blue, <strong>strong</strong> paragraph</p>'
    )
    assert received.body == "This is a simple text"


def test_multiple_emails_send(mailoutbox):
    html = '<p style="color:blue;font-size:46px;">I\'m a big, blue, <strong>strong</strong> paragraph</p>'
    email1 = (
        EmailBuilder("sender@example.com")
        .add_receiver("receiver@example.com")
        .add_text("This is a simple text")
        .add_subject("Test subject")
        .add_html(html)
        .build_django_mail()
    )
    email2 = (
        EmailBuilder("sender@example.com")
        .add_receiver("receiver@example.com")
        .add_text("This is a simple text")
        .add_subject("Test subject")
        .build_django_mail()
    )

    emails = [email1, email2]

    mail.get_connection().send_messages(emails)

    assert len(mailoutbox) == 2, "Got 2 messages"
    for m in mailoutbox:
        assert m.body == "This is a simple text"

    print(mailoutbox[0].message().as_string())
