from django.db import models

from django.utils.timezone import now

# Models
class Date(models.Model):
    created = models.DateTimeField("Created Date", default=now, editable=False)
    updated = models.DateTimeField("Date Updated", default=now, editable=False)

    class Meta:
        abstract = True

class Email(Date):  
    email = models.EmailField('Email', max_length=50, unique=True)

class Phone(Date):
    phone = models.CharField('Phone', max_length=50)

class Address(Date):
    street1 = models.CharField('Street', max_length=50, blank=True, null=True)
    street2 = models.CharField('Street 2', max_length=50, blank=True, null=True)
    city = models.CharField('City', max_length=50, blank=True, null=True)
    state = models.CharField('State', max_length=50, blank=True, null=True)
    zipcode = models.CharField('Zip Code', max_length=5, blank=True)
    lat = models.FloatField('Latitude', null=True, default=None, blank=True)
    lng = models.FloatField('Longitude', null=True, default=None, blank=True)

class Contact(Date):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    phone_id = models.ManyToManyField(Phone, blank=True, related_name='phone_contact')
    email_id = models.ManyToManyField(Email, blank=True, related_name='email_contact')
    address_id = models.ManyToManyField(Address, blank=True, related_name='address_contact')

class Place(Date):
    name = models.CharField('Place Name', max_length=50)
    type = models.CharField('Place Type', max_length=50)
    phone_id = models.ManyToManyField(Phone, blank=True, related_name='phone_place')
    email_id = models.ManyToManyField(Email, blank=True, related_name='email_place')
    address_id = models.ManyToManyField(Address,blank=True, related_name='address_place')