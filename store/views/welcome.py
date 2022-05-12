from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

class Welcome(View):
    def get(self,request):
        return render(request,'welcome.html')