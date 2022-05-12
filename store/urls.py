from store import views
from store.views.welcome import Welcome
from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.welcome import Welcome
from .views.designerlogin import Designer,deslogout
from .views.adddesign import add
from .views.requesteddesign import reqDesign
from .views.payment import Payment
from .views import profile



urlpatterns = [
    path('store', store , name='store'),
    path('', Index.as_view(), name='homepage'),
    path('Add_Requests', Designer.addreq, name='addrequest'),
    path('add_design',add,name="adddesign"),
    path('requested_design',reqDesign.as_view(),name="reqdesign"),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('Designer/Home',Designer.home,name='deshome'),
    path('dlogout', deslogout , name='deslogout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('updpass',profile.updpass,name='updpass'),
    path('MyProfile',profile.add,name='myprofile'),
    path('payment',Payment.as_view(),name='payment'),
    path('dlogin',Designer.as_view(),name='deslogin'),
    path('deleteacc',profile.deleteacc,name='deleteacc'),
    path('deletepage',profile.delpage,name='deletepage')
]
