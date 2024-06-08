from django.db import models

# Create your models here.

class ContactDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Subject = models.CharField(max_length=150,null=True,blank=True)
    Message = models.TextField(null=True,blank=True)

class User_Account(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)

class CartDB(models.Model):
    UserName = models.CharField(max_length=100,null=True,blank=True)
    Product = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(max_length=100,null=True,blank=True)
    TotalPrice = models.IntegerField(max_length=100,null=True,blank=True)

class PaymentDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Town = models.CharField(max_length=100,null=True,blank=True)
    PIN = models.CharField(max_length=100,null=True,blank=True)
    Mobile = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
