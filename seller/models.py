from django.db import models

# Create your models here.
class sregister_tb(models.Model):
   name=models.CharField(max_length=20)
   address=models.CharField(max_length=20)
   gender=models.CharField(max_length=20)
   dob=models.CharField(max_length=20)
   phone=models.CharField(max_length=20)
   country=models.CharField(max_length=20)
   username=models.CharField(max_length=20)
   password=models.CharField(max_length=20)
   file=models.FileField()
   status=models.CharField(max_length=20,default="pending")
class product_tb(models.Model):
   productname=models.CharField(max_length=20)
   image=models.FileField()
   price=models.IntegerField()
   stock=models.IntegerField()
   categoryid=models.ForeignKey("siteadmin.category_tb",on_delete=models.CASCADE)
   sellerid=models.ForeignKey(sregister_tb,on_delete=models.CASCADE)
   details=models.CharField(max_length=20,default="abc")
class tracking_tb(models.Model):
   orderid=models.ForeignKey("buyer.order_tb",on_delete=models.CASCADE)
   date=models.CharField(max_length=20)
   time=models.CharField(max_length=20)
   details=models.CharField(max_length=20)
