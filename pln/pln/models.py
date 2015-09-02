# models.py

from django.db import models

class Application(models.Model):
    category = models.CharField(max_length=128)

class Platform(models.Model):
    category = models.CharField(max_length=128)

class Function(models.Model): 
    category = models.CharField(max_length=128)

class Price(models.Model):
    category = models.CharField(max_length=128)

class Support(models.Model):
    category = models.CharField(max_length=128)

class PLNTool(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=128)
    url = models.URLField(blank=True)
    privacy = models.CharField(max_length=128, blank=True)
    tutorial = models.CharField(max_length=128, blank=True)
    platform = models.ManyToManyField(Platform, blank=True)
    application = models.ManyToManyField(Application, blank=True) 
    function = models.ManyToManyField(Function, blank=True)
    price = models.ManyToManyField(Price, blank=True)
    support = models.ManyToManyField(Support, blank=True)

class Testimonial(models.Model):
    text = models.TextField()
    tool = models.ForeignKey(PLNTool)

