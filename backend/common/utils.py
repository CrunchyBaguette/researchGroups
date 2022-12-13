# from django.contrib.sites.shortcuts import get_current_site
# from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken

# from rest_framework.request import Request
from django.utils.http import urlencode
from django.conf import settings
from backend.utilsx.mail.EmailBuilder import EmailBuilder


def get_registration_email(user: User, link: str) -> EmailMultiAlternatives:
    return (
        EmailBuilder(settings.EMAIL_HOST_USER)
        .add_text(get_email_body_for_user(user, link))
        .add_receiver(user.email)
        .add_subject("Activate account")
        .build_django_mail()
    )


def generate_registration_link(token: AccessToken) -> str:
    # current_site = get_current_site(request).domain
    # relative_link = reverse("register")
    url = f"http://localhost:8080/#/login/?{urlencode({'token': token})}"

    return url


def get_email_body_for_user(user: User, link: str) -> str:
    return f"Hi {user.first_name} {user.last_name} \nUse this link to activate your account: {link}"


def get_email_body_for_reset(user: User, link: str) -> str:
    return f"""Hi {user.first_name} {user.last_name} \nUse this link to reset your password: {link}
    
    Link will be active for 30 minutes"""


def generate_reset_pass_link(token: AccessToken) -> str:
    # current_site = get_current_site(request).domain
    # relative_link = reverse("reset-pass")
    url = f"http://localhost:8080/#/login/password-reset/?{urlencode({'token': token})}"

    return url


def get_reset_pass_email(user: User, link: str) -> EmailMultiAlternatives:
    return (
        EmailBuilder(settings.EMAIL_HOST_USER)
        .add_text(get_email_body_for_reset(user, link))
        .add_receiver(user.email)
        .add_subject("Reset password")
        .build_django_mail()
    )
