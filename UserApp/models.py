from django.db import models
from AdminApp . models import *

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100,default='null')
    email = models.EmailField(max_length=100,default='null')
    password = models.CharField(max_length=100,default='null')
    phone = models.CharField(max_length=100,default=0)
    place = models.TextField(default='null')
    status = models.IntegerField(default=0)
class Contact(models.Model):
    name = models.CharField(max_length=100,default='null')
    email = models.EmailField(max_length=100,default='null')
    phone = models.CharField(max_length=100,default=0)
    subject = models.CharField(max_length=20,default='null')
    message = models.TextField(default='null')
class Cart(models.Model):
    usercart = models.ForeignKey(Register,on_delete=models.CASCADE)
    userpro  = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.IntegerField()
    status = models.IntegerField(default=0)
class Checkout(models.Model):
    usercheckout = models.ForeignKey(Register,on_delete=models.CASCADE)
    usercart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    adress = models.TextField()
    city = models.CharField(max_length=20)
    pincode = models.IntegerField()
    country = models.CharField(max_length=20)
