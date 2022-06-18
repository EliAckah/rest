from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class Volunteer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    phone_number = PhoneNumberField(null=True)
    Why_you_want_to_volunteer = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name + " -- " + str(self.phone_number)

class Executive(models.Model):
    name = models.CharField(max_length=200,null=True)
    exexcutive_pos = models.CharField(max_length=200,null=True)
    exec_pic = models.ImageField(null=True,default="avatar.svg")
    whatsapp_url = models.CharField(max_length=200,null=True)
    facebook_url = models.CharField(max_length=200,null=True)
    instagram_url = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Cause(models.Model):
    cause_title = models.CharField(max_length=200,null=True)
    cause_body = models.TextField(null=True)
    slug = models.SlugField(null=False,unique=True)
    cause_pic = models.ImageField(null=True,default="avatar.svg")

    def __str__(self):
        return self.cause_title
    
    def get_absolute_url(self):
        return reverse("cause_detail", kwargs={"slug": self.slug})

class Event(models.Model):
    event_title = models.CharField(max_length=200,null=True)
    event_body = models.TextField(null=True)
    event_date = models.CharField(max_length=200,null=True)
    event_time = models.CharField(max_length=200,null=True)
    event_location = models.CharField(max_length=200,null=True)
    event_pic = models.ImageField(null=True,default="avatar.svg")
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.event_title
    
    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"slug": self.slug})
    
class JoinEvent(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    phone_number = PhoneNumberField(null=True)
    event_to_join = models.ForeignKey(Event, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name + " -- " + str(self.event_to_join)
