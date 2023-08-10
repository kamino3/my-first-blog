
from django.contrib import admin
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC

admin.site.register(EmailConfirmation)
admin.site.register(EmailConfirmationHMAC)
