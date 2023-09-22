# import datetime
from django.db import models


# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    # birthdate = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
