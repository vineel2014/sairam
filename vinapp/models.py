from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    name=models.CharField(max_length=120,unique=True)
    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):    #for python2 use __unicode__ too.
        return self.name

class Page(models.Model):
    category=models.ForeignKey(Category)
    title=models.CharField(max_length=120)
    url=models.URLField()
    views=models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):

    user=models.OneToOneField(User)

    website=models.URLField(blank=True)

    picture=models.ImageField(upload_to='profile_images',blank=True)

    def __univode__(self):
        return self.user.username


