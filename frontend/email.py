from evc.settings import DEFAULT_FROM_EMAIL
from django.template import Context, context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def send_contact_email(name, email, website, phone, message, date):
    context = {
        'name': name,
        'email': email,
        'website': website,
        'phone': phone,
        'message': message,
        'date' : date,
    }

    email_subject = 'Thank You For Contacting Us'
    email_body = render_to_string('email_message.txt', context)

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email,]
    )
    return email.send(fail_silently=True)