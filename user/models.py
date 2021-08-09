from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    dob = models.DateField(max_length=8, null=True)
    address = models.TextField(null=True)
    state = models.ForeignKey(State, on_delete= models.SET_NULL, null= True)
    vaccinated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username