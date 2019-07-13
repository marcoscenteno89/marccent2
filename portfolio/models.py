from django.db import models

class portfolio(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    # phone = models.CharField(max_length=50)
    # street1 = models.CharField(max_length=50)
    # street2 = models.CharField(max_length=50, blank=True)
    # city = models.CharField(max_length=50)
    # state = models.CharField(max_length=50)
    # zip = models.CharField(max_length=5)
    # message = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    