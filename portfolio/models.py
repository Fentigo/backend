from django.db import models

# Create your models here.

# Important here to understand the data types your site will need

class Poet(models.Model):
    first_name = models.CharField(max_length=140) 
    last_name = models.CharField(max_length=140) 
    dob = models.DateField(max_length=50)
    contact_info = models.CharField(max_length=12)
    description = models.TextField(max_length=2000)

class SocialMedia(models.Model):
    site = models.CharField(max_length=50)
    url = models.CharField(max_length=50)

class Bookings(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

class Video(models.Model):
    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')

class Image(models.Model):
    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=200)
    image_file = models.FileField(upload_to='images/')

