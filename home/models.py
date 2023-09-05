from django.db import models
import datetime

# Create your models here.
class Customer(models.Model):
    cust_id = models.AutoField
    cust_name = models.CharField(max_length=50)
    cust_mail = models.CharField(max_length=50)
    cust_number = models.CharField(max_length=10)

    def __str__(self):
        return self.cust_name 
