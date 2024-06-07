from django.db import models

# Create your models here.
class Category_DB(models.Model):
     Category_Name = models.CharField(max_length=100,null=True,blank=True)
     Category_Description = models.TextField(null=True,blank=True)
     Category_Image = models.ImageField(upload_to="Category Images",null=True,blank=True)


class Product_DB(models.Model):
     Product = models.CharField(max_length=100,null=True,blank=True)
     Category = models.CharField(max_length=100,null=True,blank=True)
     Description = models.TextField(null=True,blank=True)
     Price  = models.CharField(max_length=100,null=True,blank=True)
     Image = models.ImageField(upload_to="Product Image",null=True,blank=True)