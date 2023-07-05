from django.shortcuts import render,redirect
from siteadmin.models import*
from buyer.models import*
from seller.models import*
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
   return render(request,"login.html")
def loginaction(request):
    username=request.POST['username']
    password=request.POST['password']
    user=admin_tb.objects.filter(username=username,password=password)
    buyer=register_tb.objects.filter(username=username,password=password)
    seller=sregister_tb.objects.filter(username=username,password=password)
    
    if user.count()>0:
        request.session['id']=user[0].id
        return render(request,"loginhome.html")
    
    elif buyer.count()>0:
        request.session['id']=buyer[0].id
        return render(request,"buyerhome.html")
    elif seller.count()>0:
         status=seller[0].status
         if status=='approved':
            request.session['id']=seller[0].id
            return render(request,'sellerhome.html')
         elif status=='rejected':
            return redirect('login')
         else:
            messages.add_message(request,messages.INFO,"Waiting for approval")
            return redirect('index')
    
    else:
        return redirect('index')
def category(request):
   return render(request,"category.html")
def categoryaction(request):
    name=request.POST['name']
    user=category_tb(cname=name)
    user.save()
    messages.add_message(request,messages.INFO,"category added")
    return redirect('category')
def viewseller(request):
    seller=sregister_tb.objects.filter(status='pending')
    return render(request,"viewseller.html",{'se':seller})
def details(request,id):
    d=sregister_tb.objects.filter(id=id)
    return render(request,"sellerdetails.html",{'de':d})
def approve(request,id):
    ap=sregister_tb.objects.filter(id=id).update(status="approved")
    return redirect('viewseller')
def reject(request,id):
    re=sregister_tb.objects.filter(id=id).update(status="rejected")
    return redirect('viewseller')
def logout(request):
    request.session.flush()
    return redirect('index')
    
    
