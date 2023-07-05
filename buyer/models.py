from django.db import models


# Create your models here.
class register_tb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class cart_tb(models.Model):
    buyerid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    productid=models.ForeignKey("seller.product_tb",on_delete=models.CASCADE)
    shippingaddress=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    quantity=models.IntegerField()
    totalprice=models.IntegerField()
class order_tb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    orderdate=models.CharField(max_length=20,default="pending")
    ordertime=models.CharField(max_length=20,default="pending")  
    buyerid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,default="pending")
class orderitem_tb(models.Model):
    quantity=models.IntegerField()
    totalprice=models.IntegerField()
    productid=models.ForeignKey("seller.product_tb",on_delete=models.CASCADE)
    buyerid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    orderid=models.ForeignKey(order_tb,on_delete=models.CASCADE)
class payment_tb(models.Model):
    cardname=models.CharField(max_length=20)
    cardnumber=models.CharField(max_length=20)
    cvv=models.IntegerField()
    expirydate=models.CharField(max_length=20)
    orderid=models.ForeignKey(order_tb,on_delete=models.CASCADE)
    buyerid=models.ForeignKey(register_tb,on_delete=models.CASCADE)

