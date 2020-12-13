from django import forms
from .models import Contact
from django.core.mail import EmailMessage
from django.conf import settings

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ("__all__")
        exclude = ("date",)
    
    def send_email(self):
        
        name = self.cleaned_data['name'] 
        email = self.cleaned_data['email']
        website = self.cleaned_data['website'] 
        phone = self.cleaned_data['phone'] 
        message = self.cleaned_data['message']

        subject = "Thank you for contacting us"
        body = f'Here is a copy of the information you sent to us:\n Name = {name}, \n Email = {email} \n Website = {website} \n Phone: {phone} \n Message = {message}'
        email = EmailMessage(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [email,]
        )
        print(body)
        return email.send(fail_silently=False)