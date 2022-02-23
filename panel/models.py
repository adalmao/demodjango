from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(null=False,blank=False,max_length=250)
	last_name = models.CharField(null=False,blank=False,max_length=250)
	email = models.CharField(null=False,blank=False,max_length=250)