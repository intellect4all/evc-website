from celery.decorators import task
from .email import send_contact_email

@task(name="send_contact_email_task")
def send_contact_email_task(name, email, website, phone, message, date):
    return send_contact_email(name, email, website, phone, message, date)

