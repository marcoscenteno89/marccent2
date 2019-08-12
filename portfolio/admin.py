from django.contrib import admin
from .models import Contact, Phone, Email, Address

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']