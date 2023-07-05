from django.shortcuts import render,redirect
from siteadmin.models import*
from buyer.models import*
from seller.models import*
from django.contrib import messages
import datetime
# Create your views here.
def register(request):
    return render(request,"register.html")
def registeraction(request):
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    dob=request.POST['dob']
    phone=request.POST['phone']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb(name=name,address=address,gender=gender,dob=dob,phone=phone,country=country,username=username,password=password)
    user.save()
    messages.add_message(request,messages.INFO,"registration successfull")
    return redirect('register')
def buyerupdate(request):
    buyer=request.session['id']
    buyid=register_tb.objects.filter(id=buyer)
    return render(request,"buyeredit.html",{'buy':buyid})
def buyereditAction(request):
    buyer=request.session['id']
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    dob=request.POST['dob']
    phone=request.POST['phone']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']
    buyer=register_tb.objects.filter(id=buyer).update(name=name,address=address,gender=gender,dob=dob,phone=phone,country=country,username=username,password=password)
    return redirect('buyerupdate')
def product(request):
    product=product_tb.objects.all()
    return render(request,"product.html",{'pro':product})
def addtocart(request,id):
    a=product_tb.objects.filter(id=id)
    return render(request,"cartnew.html",{'cart':a})
def cartaction(request):
    buyer=request.session['id']
    productid=request.POST['productid']
    shippingaddress=request.POST['shippingaddress']
    quantity=request.POST['quantity']
    phone=request.POST['phone']
    total=request.POST['total']
    stock=request.POST['stock']
    if int(quantity)< int(stock):
        car=cart_tb(shippingaddress=shippingaddress,quantity=quantity,phone=phone,totalprice=total,buyerid_id=buyer,productid_id=productid)
        car.save()
    else:
        messages.add_message(request,messages.INFO,"Quantity greater than stock")
    return redirect('product')
def viewcart(request):
    buyer=request.session['id']
    cart=cart_tb.objects.filter(buyerid=buyer)
    return render(request,"viewcart1.html",{'ca':cart})
def cartdelete(request,id):
    d=cart_tb.objects.filter(id=id).delete()
    return redirect('viewcart')
def placeorder(request):
    name=request.POST['customername']
    address=request.POST['shippingaddress']
    phone=request.POST['phone']
    orderdate=datetime.date.today()
    ordertime=datetime.datetime.now().strftime("%H : %M")
    buyerid=request.session['id']
    cartitems=request.POST.getlist('checkbox')
    if len(cartitems)!= 0:
        o=order_tb(name=name,address=address,orderdate=orderdate,ordertime=ordertime,phone=phone,buyerid_id=buyerid)
        o.save()
        for cid in cartitems:
            cart=cart_tb.objects.filter(id=cid)
            qty=cart[0].quantity
            tot=cart[0].totalprice
            productid=cart[0].productid_id
            stock=cart[0].productid.stock
            newstock=int(stock)-qty
            product=product_tb.objects.filter(id=productid).update(stock=newstock)
            cart.delete()
            orderitem=orderitem_tb(quantity=qty,totalprice=tot,productid_id=productid,buyerid_id=buyerid,orderid_id=o.id)
            orderitem.save()
        return redirect('paynow',o.id)
    else:
        messages.add_message(request,messages.INFO,"select atleast one item")
    return redirect('product')
def orderdetails(request):
    order=order_tb.objects.filter(buyerid=request.session['id'])
    orderitem=orderitem_tb.objects.filter(orderid_id=order[0].id).select_related('orderid').values('orderid_id')
    return render(request,"orderdetails.html",{'or':order})
def odetails(request,id):
    orderitem=orderitem_tb.objects.filter(orderid_id=id,buyerid=request.session['id']).select_related('orderid')
    order=order_tb.objects.filter(id=id)
    return render(request,"orderview.html",{'ord':order,'or':orderitem})
def cancelorder(request,id):
    order=order_tb.objects.filter(id=id).update(status="cancelled")
    return redirect('viewcart')
def viewtrackingdetail(request,id):
    track=tracking_tb.objects.filter(orderid=id)
    return render(request,"viewtrackingdetail.html",{'tr':track})
def paynow(request,id):
    order=orderitem_tb.objects.filter(orderid=id)
    return render(request,"payment.html",{'ord':order})
def payaction(request):
    name=request.POST['cardname']
    cno=request.POST['cardnumber']
    cvv=request.POST['cvv']
    date=request.POST['expirydate']
    orderid=request.POST['orderid']
    buyer=request.session['id']
    pay=payment_tb(cardname=name,cardnumber=cno,cvv=cvv,expirydate=date,orderid_id=orderid,buyerid_id=buyer)
    pay.save()
    return redirect('product')
def searchproduct(request):
    return render(request,"searchproduct.html")
def searchaction(request):
    name=request.POST['productname']
    prod=product_tb.objects.filter(productname__istartswith=name)
    return render(request,"product.html",{'pro':prod})
def searchcategory(request):
    cat=category_tb.objects.all()
    return render(request,"searchcategory.html",{'ct':cat})
def searchcategoryaction(request):
    cat=request.POST['category']
    price=request.POST['price']
    prod=product_tb.objects.filter(price__gte=price,categoryid_id=cat)
    return render(request,"product.html",{'pro':prod})
def forgotpassword(request):
    return render(request,"forgotpassword.html")
def forgotpasswordaction(request):
    name=request.POST['username']
    seller=sregister_tb.objects.filter(username=name)
    print(seller)
    buyer=register_tb.objects.filter(username=name)
    print(buyer)
    if seller.count()>0:
        return render(request,"forgotpswdaction.html",{'data':name})
    elif buyer.count()>0:
         return render(request,"forgotpswdaction.html",{'data':name})
    else:
        return redirect('index')
def resetpassword(request):
    uname=request.POST['username']
    name=request.POST['name']
    dob=request.POST['dob']
    country=request.POST['country']
    seller=sregister_tb.objects.filter(username=uname,name=name,dob=dob,country=country)
    print(seller)
    buyer=register_tb.objects.filter(username=uname,name=name,dob=dob,country=country)
    print(buyer)
    if seller.count()>0:
        return render(request,"resetpassword.html",{'data':uname})
    elif buyer.count()>0:
        return render(request,"resetpassword.html",{'data':uname})
    else:
        return redirect('index')
def resetpasswordaction(request):
    uname=request.POST['username']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    if newpassword == confirmpassword:
        seller=sregister_tb.objects.filter(username=uname)
        buyer=register_tb.objects.filter(username=uname)
        if seller.count()>0:
            request.session['id']=seller[0].id
            sellerid=request.session['id']
            
            sell=sregister_tb.objects.filter(id=sellerid).update(password=newpassword)
            messages.add_message(request,messages.INFO,"Password changed successfully")
            
        else:
            request.session['id']=buyer[0].id
            buyerid=request.session['id']
            
            buy=register_tb.objects.filter(id=buyerid).update(password=newpassword)
        messages.add_message(request,messages.INFO,"Password changed successfully")
        return redirect('index')
    else:
        messages.add_message(request,messages.INFO,"Passwords do not match")
        return render(request,"resetpassword.html",{'data':uname})

