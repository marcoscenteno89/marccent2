from django.db import models

# Models
class Contact(models.Model):
    fname = models.CharField('First Name', max_length=50)
    lname = models.CharField('Last Name', max_length=50)
    contact_date_created = models.DateTimeField('Date Created', auto_now_add=True, blank=True, null=True)

class Email(Contact):
    email_contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING, db_constraint=False)
    email = models.EmailField('Email', max_length=50, unique=True)
    email_date_created = models.DateTimeField('Date Created', auto_now_add=True, blank=True, null=True)

class Phone(Contact):
    phone_contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING, db_constraint=False)
    phone = models.CharField('Phone', max_length=50)
    phone_date_created = models.DateTimeField('Date Created', auto_now_add=True, blank=True, null=True)

class Address(Contact):
    address_contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING, db_constraint=False)
    street1 = models.CharField('Street', max_length=50)
    street2 = models.CharField('Street 2', max_length=50, blank=True)
    city = models.CharField('City', max_length=50)
    state = models.CharField('State', max_length=50)
    zipcode = models.CharField('Zip Code', max_length=5)
    lat = models.FloatField('Latitude', null=True, default=None)
    lng = models.FloatField('Longitude', null=True, default=None)
    adddress_date_created = models.DateTimeField('Date Created', auto_now_add=True, blank=True, null=True)
