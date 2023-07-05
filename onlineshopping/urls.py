"""onlineshopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seller import views as sellerview
from buyer import views as buyerview
from siteadmin import views as adminview
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name="index"),
    path('login/',adminview.login,name="login"),
    path('loginaction/',adminview.loginaction,name="loginaction"),
    path('category/',adminview.category,name="category"),
    path('categoryaction/',adminview.categoryaction,name="categoryaction"),
    path('register/',buyerview.register,name="register"),
    path('registeraction/',buyerview.registeraction,name="registeraction"),
    path('sregister/',sellerview.sregister,name="sregister"),
    path('sregisteraction/',sellerview.sregisteraction,name="sregisteraction"),
    path('buyerupdate/',buyerview.buyerupdate,name="buyerupdate"),
    path('buyereditaction/',buyerview.buyereditAction,name="buyereditaction"),
    path('viewseller/',adminview.viewseller,name="viewseller"),
    path('details<int:id>/',adminview.details,name="details"),
    path('approve<int:id>/',adminview.approve,name="approve"),
    path('reject<int:id>/',adminview.reject,name="reject"),
    path('sellerupdate/',sellerview.sellerupdate,name="sellerupdate"),
    path('sellereditaction/',sellerview.sellereditaction,name="sellereditaction"),
    path('addproduct/',sellerview.addproduct,name="addproduct"),
    path('productaction/',sellerview.productaction,name="productaction"),
    path('productview/',sellerview.productview,name="productview"),
    path('productdelete<int:id>/',sellerview.productdelete,name="productdelete"),
    path('productedit<int:id>/',sellerview.productedit,name="productedit"),
    path('producteditaction/',sellerview.producteditaction,name="producteditaction"),
    path('product/',buyerview.product,name="product"),
    path('addtocart<int:id>/',buyerview.addtocart,name="addtocart"),
    path('cartaction/',buyerview.cartaction,name="cartaction"),
    path('viewcart/',buyerview.viewcart,name="viewcart"),
    path('cartdelete<int:id>/',buyerview.cartdelete,name="cartdelete"),
    path('placeorder/',buyerview.placeorder,name="placeorder"),
    path('orderdetails/',buyerview.orderdetails,name="orderdetails"),
    path('odetails<int:id>/',buyerview.odetails,name="odetails"),
    path('viewbuyerorder/',sellerview.viewbuyerorder,name="viewbuyerorder"),
    path('svodetails<int:id>/',sellerview.svodetails,name="svodetails"),
    path('sapprove<int:id>/',sellerview.sapprove,name="sapprove"),
    path('sreject<int:id>/',sellerview.sreject,name="sreject"),
    path('cancelorder<int:id>/',buyerview.cancelorder,name="cancelorder"),
    path('trackingdetails<int:id>/',sellerview.trackingdetails,name="trackingdetails"),
    path('trackaction/',sellerview.trackaction,name="trackaction"),
    path('viewtrackingdetail<int:id>/',buyerview.viewtrackingdetail,name="viewtrackingdetail"),
    path('confirmcancel<int:id>/',sellerview.confirmcancel,name="confirmcancel"),
    path('paynow<int:id>/',buyerview.paynow,name="paynow"),
    path('payaction/',buyerview.payaction,name="payaction"),
    path('searchproduct/',buyerview.searchproduct,name="searchproduct"),
    path('searchaction/',buyerview.searchaction,name="searchaction"),
    path('searchcategory/',buyerview.searchcategory,name="searchcategory"),
    path('searchcategoryaction/',buyerview.searchcategoryaction,name="searchcategoryaction"),
    path('forgotpassword/',buyerview.forgotpassword,name="forgotpassword"),
    path('forgotpasswordaction/',buyerview.forgotpasswordaction,name="forgotpasswordaction"),
    path('resetpassword/',buyerview.resetpassword,name="resetpassword"),
    path('resetpasswordaction/',buyerview.resetpasswordaction,name="resetpasswordaction"),
    path('logout/',adminview.logout,name="logout")
]
if settings.DEBUG:urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
