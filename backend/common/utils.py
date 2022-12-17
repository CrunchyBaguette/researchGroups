from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.request import Request
from django.utils.http import urlencode
from django.conf import settings
from backend.utilsx.mail.EmailBuilder import EmailBuilder


def get_registration_email(user: User, link: str) -> EmailBuilder:
    return (
        EmailBuilder(
            sender=settings.EMAIL_HOST_USER,
            recipient=user.email,
            subject="Aktywuj konto",
            message=get_email_body_for_user(user, link),
        )
        # EmailBuilder(settings.EMAIL_HOST_USER)
        # .add_text(get_email_body_for_user(user, link))
        # .add_receiver(user.email)
        # .add_subject("Activate account")
        # .build_django_mail()
    )


def get_reset_pass_email(user: User, link: str) -> EmailBuilder:
    return (
        EmailBuilder(
            sender=settings.EMAIL_HOST_USER,
            recipient=user.email,
            subject="Reset hasła",
            message=get_email_body_for_reset(user, link),
        )
        # EmailBuilder(settings.EMAIL_HOST_USER)
        # .add_text(get_email_body_for_reset(user, link))
        # .add_receiver(user.email)
        # .add_subject("Reset password")
        # .build_django_mail()
    )


def get_announcement_email(userTo: str, userFrom: str, message: str, announcementName: str, link: str) -> EmailBuilder:
    return EmailBuilder(
        sender=settings.EMAIL_HOST_USER,
        recipient=userTo,
        subject=f"Odpowiedź na twoje ogłoszenie ({announcementName})",
        message=get_email_body_for_announcement(userFrom, message, announcementName, link),
    )


def get_research_group_email(
    userTo: str, userFrom: str, subject: str, message: str, research_group_name: str, link: str
) -> EmailBuilder:
    return EmailBuilder(
        sender=settings.EMAIL_HOST_USER,
        recipient=userTo,
        subject=subject,
        message=get_email_body_for_research_group(userFrom, message, research_group_name, link),
    )


def get_project_email(
    userTo: str, userFrom: str, subject: str, message: str, project_name: str, link: str
) -> EmailBuilder:
    return EmailBuilder(
        sender=settings.EMAIL_HOST_USER,
        recipient=userTo,
        subject=subject,
        message=get_email_body_for_research_group(userFrom, message, project_name, link),
    )


def generate_registration_link(token: AccessToken, request: Request) -> str:
    current_site = get_current_site(request).domain
    relative_link = reverse("register")
    url = f"http://{current_site}{relative_link}?{urlencode({'token': token})}"

    return url


def get_email_body_for_user(user: User, link: str) -> str:
    return f"Cześć {user.first_name} {user.last_name} \nUżyj tego linku aby aktywować swoje konto: {link}"


def get_email_body_for_reset(user: User, link: str) -> str:
    return f"""Cześć {user.first_name} {user.last_name} \nUżyj tego linku aby zresetować swoje hasło: {link}
    
    Link będzie aktywny 30 minut."""


def get_email_body_for_announcement(userFrom: str, message: str, announcementName: str, link: str) -> str:
    return f"Od: {userFrom}\n\nOgłoszenie:\n{announcementName}\n{link}\n\n{message}"


def get_email_body_for_research_group(userFrom: str, message: str, research_group_name: str, link: str) -> str:
    return f"Od: {userFrom}\n\nKoło naukowe:\n{research_group_name}\n{link}\n\n{message}"


def get_email_body_for_project(userFrom: str, message: str, project_name: str, link: str) -> str:
    return f"Od: {userFrom}\n\nProjekt:\n{project_name}\n{link}\n\n{message}"


def generate_announcement_link(announcementId: int) -> str:
    return f"http://localhost:8080/#/announcement/{announcementId}"


def generate_research_group_link(researchGroupId: int) -> str:
    return f"http://localhost:8080/#/group/{researchGroupId}"


def generate_project_link(projectId: int) -> str:
    return f"http://localhost:8080/#/project/{projectId}"


def generate_reset_pass_link(token: AccessToken, request: Request) -> str:
    current_site = get_current_site(request).domain
    relative_link = reverse("reset-pass")
    url = f"http://{current_site}{relative_link}?{urlencode({'token': token})}"

    return url
