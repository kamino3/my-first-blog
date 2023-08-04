
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views import View
from django.conf import settings

class ContactView(View):
    def get(self, request):
        return render(request, 'contact/contact.html')

    def post(self, request):
        # Get the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create the email message
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n\n{message}"

        # Send the email
        send_mail(
            subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            ['naaaaki@gmail.com']
        )

        # Redirect to the home page
        return redirect('/')
