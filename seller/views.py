from django.shortcuts import render,redirect
from siteadmin.models import*
from buyer.models import*
from seller.models import*
from django.contrib import messages
import datetime
# Create your views here.
def sregister(request):
    return render(request,"sregister.html")
def sregisteraction(request):
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    dob=request.POST['dob']
    phone=request.POST['phone']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']
    if len(request.FILES)>0:
        img=request.FILES['file']
    else:
        img="no pic"
    user=sregister_tb(name=name,address=address,gender=gender,dob=dob,phone=phone,country=country,username=username,password=password,file=img)
    user.save()
    messages.add_message(request,messages.INFO,"registration successfull")
    return redirect('sregister')
def sellerupdate(request):
    seller=request.session['id']
    sellid=sregister_tb.objects.filter(id=seller)
    return render(request,"selleredit.html",{'sell':sellid})
def sellereditaction(request):
    seller=request.session['id']
    sellid=sregister_tb.objects.filter(id=seller)
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    dob=request.POST['dob']
    phone=request.POST['phone']
    country=request.POST['country']

    if len(request.FILES)>0:
        img=request.FILES['file']
        
    else:
        img=sellid[0].file
    username=request.POST['username']
    password=request.POST['password']
    seller=sregister_tb.objects.filter(id=seller).update(name=name,address=address,gender=gender,dob=dob,phone=phone,country=country,username=username,password=password)
    seller_object=sregister_tb.objects.get(id=seller)
    seller_object.file=img
    seller_object.save()
    
    return redirect('sellerupdate')
def addproduct(request):
    category=category_tb.objects.all()
    return render(request,"addproduct.html",{'cat':category})
def productaction(request):
    seller=request.session['id']
    productname=request.POST['productname']
    price=request.POST['price']
    stock=request.POST['stock']
    details=request.POST['details']
    categoryid=request.POST['categoryid']
    if len(request.FILES)>0:
        img=request.FILES['image']
    else:
        img="no pic"
    product=product_tb(productname=productname,price=price,stock=stock,details=details,categoryid_id=categoryid,sellerid_id=seller,image=img)
    product.save()
    messages.add_message(request,messages.INFO,"Product Added")
    return redirect('addproduct')
def productview(request):
    seller=request.session['id']
    product=product_tb.objects.filter(sellerid=seller)
    return render(request,"productview.html",{'p':product})
def productdelete(request,id):
    d=product_tb.objects.filter(id=id).delete()
    return redirect('productview')
def productedit(request,id):
    e=product_tb.objects.filter(id=id)
    c=category_tb.objects.all()
    return render(request,"productedit.html",{'edit':e,'ce':c})
def producteditaction(request):
    product=request.POST['id']
    productid=product_tb.objects.filter(id=product)
    productname=request.POST['productname']
    if len(request.FILES)>0:
        img=request.FILES['image']
    else:
        img=productid[0].image
    price=request.POST['price']
    stock=request.POST['stock']
    details=request.POST['details']
    categoryid=request.POST['categoryid']
    sellerid=request.POST['sellerid']
    pro=product_tb.objects.filter(id=product).update(productname=productname,image=img,price=price,stock=stock,details=details,
                                                     categoryid_id=categoryid,sellerid_id=sellerid)
    p=product_tb.objects.get(id=product)
    p.image=img
    p.save()
    return redirect('productedit')
def viewbuyerorder(request):
    seller=product_tb.objects.filter(sellerid=request.session['id']).values('id')
    orderitem=orderitem_tb.objects.filter(productid_id__in=seller).select_related('orderid').values('orderid_id')
    order=order_tb.objects.filter(id__in=orderitem)
    return render(request,"viewbuyerorder.html",{'or':order})
def svodetails(request,id):
    sp=product_tb.objects.filter(sellerid=request.session['id']).values('id')
    orderitem=orderitem_tb.objects.filter(orderid=id,productid_id__in=sp).select_related('orderid')
    order=order_tb.objects.filter(id=id)
    return render(request,"sellerorderdetails.html",{'or':order,'ord':orderitem})
def sapprove(request,id):
    ord=order_tb.objects.filter(id=id).update(status="approved")
    return redirect('viewbuyerorder')
def sreject(request,id):
    ord=order_tb.objects.filter(id=id).update(status="rejected")
    return redirect('viewbuyerorder')
def trackingdetails(request,id):
    order=order_tb.objects.filter(id=id)
    return render(request,"tracking.html",{'ord':order})
def trackaction(request):
    id=request.POST['orderid']
    orderid=order_tb.objects.get(id=id)
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H : %M")
    details=request.POST['details']
    track=tracking_tb(date=date,time=time,details=details,orderid=orderid)
    track.save()
    return redirect('viewbuyerorder')
def confirmcancel(request,id):
    ord=orderitem_tb.objects.filter(orderid=id)
    for v in ord:
        pro=product_tb.objects.filter(id=v.productid_id)
        qty=v.quantity
        stock=pro[0].stock
        newstock=stock+qty
        product=product_tb.objects.filter(id=v.productid_id).update(stock=newstock)
    order_tb.objects.filter(id=id).update(status="cancelled")
    return redirect('viewbuyerorder')
    
