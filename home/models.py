# import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.http import request
#if you dont want any model feature to be required add blank=True


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
    
class QuizSubmissions(models.Model):
    feeling_overwhelmed = models.CharField(max_length=201)
    being_judged = models.CharField(max_length=20)
    sleep_patterns = models.CharField(max_length=20)
    confront_challenges = models.CharField(max_length=20)
    comfortable_enclosed_spaces = models.CharField(max_length=100)
    public_speaking_anxiety = models.CharField(max_length=201)
    anxiety_in_crowded_places = models.CharField(max_length=100)
    fear_of_missing_out = models.CharField(max_length=20)
    panic_or_fear = models.CharField(max_length=20)
    are_you_satisfied_with_work_life = models.CharField(max_length=210)
    difficulty_concentrating = models.CharField(max_length=201)
    overthinking_decisions = models.CharField(max_length=201)

    def __str__(self):
        return f"Quiz Submission - {self.pk}"
    

class Venue(models.Model):
    name= models.CharField('Venue Name', max_length=120)
    address= models.CharField(max_length=300)
    zip_code= models.CharField('Zip code', max_length=15)
    phone= models.CharField('Contact Phone', max_length=12)
    web= models.URLField('Website Address')
    email_address=models.EmailField('Email Address')
    owner=models.IntegerField("Venue Owner", blank=False, default=1)
    venue_image=models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.name
    
class MindDocEventUser(models.Model):
    first_name= models.CharField(max_length=120)
    last_name= models.CharField(max_length=120)
    email= models.EmailField('Email Address')

    def __str__(self):
        return self.first_name+' '+self.last_name

class Event(models.Model):
    name= models.CharField('Event Name', max_length=120)
    event_date= models.DateTimeField('Event Date')
    venue=models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)#one to one or  one to many 
    # venue=models.CharField(max_length=120)
    manager= models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description= models.TextField(blank=True)#so we odnt have to put desc if we dont want to thats why blank=true
    attendees= models.ManyToManyField(MindDocEventUser, blank=True)

    def __str__(self):
        return self.name

    @property
    def Days_till(self):
        today=date.today()
        days_till = self.event_date.date()-today
        days_till_stripped=str(days_till).split(",", 1)[0]
        return days_till_stripped
    
    @property
    def Is_Past(self):
        today=date.today()
        if self.event_date.date()<today:
            thing="No Longer Available "
        else:
            thing="Upcoming"
        return thing

class Appointments(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=15)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ["sent_date"]

