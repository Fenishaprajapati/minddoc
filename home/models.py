# import datetime
from django.db import models
from django.contrib.auth.models import User


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
    

