from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.product import Product
from django.views import  View

class reqDesign(View):
    def get(self,request):
        return render(request,'requesteddesigns.html')