from django.db import models

# Create your models here.
class admin_tb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class category_tb(models.Model):
    cname=models.CharField(max_length=20)
