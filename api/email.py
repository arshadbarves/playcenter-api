from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email_verification(user):
    subject = 'Verify your email'
    protocol = 'https' if settings.SECURE_SSL_REDIRECT else 'http'
    domain = settings.DOMAIN_NAME
    url = protocol + '://' + domain + \
        reverse('verify_email', args=[user.email_verification_token])

    html_message = render_to_string('email/verify_email.html', {
        'protocol': protocol, 'domain': domain, 'url': url, 'site_name': settings.SITE_NAME})
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = user.email
    send_mail(subject, plain_message, from_email,
              [to], html_message=html_message)


def send_password_reset(user):
    subject = 'Reset your password'
    protocol = 'https' if settings.SECURE_SSL_REDIRECT else 'http'
    domain = settings.DOMAIN_NAME
    url = protocol + '://' + domain + \
        reverse('reset_password', args=[user.password_reset_token])

    html_message = render_to_string('email/reset_password.html', {
        'protocol': protocol, 'domain': domain, 'url': url, 'site_name': settings.SITE_NAME})
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = user.email
    send_mail(subject, plain_message, from_email,
              [to], html_message=html_message)


def send_otp_verification(user):
    subject = 'Verify your OTP'
    protocol = 'https' if settings.SECURE_SSL_REDIRECT else 'http'
    domain = settings.DOMAIN_NAME
    url = protocol + '://' + domain + \
        reverse('verify_otp', args=[user.otp_verification_token])

    html_message = render_to_string('email/verify_otp.html', {
        'protocol': protocol, 'domain': domain, 'url': url, 'site_name': settings.SITE_NAME})
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = user.email
    send_mail(subject, plain_message, from_email,
              [to], html_message=html_message)
