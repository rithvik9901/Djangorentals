from django.http.response import HttpResponse
from store.forms import ProductForm
from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.product import Product
from django.views import  View
from store.forms import *
from django.views.decorators.csrf import csrf_exempt


def add(request):
    upload = ProductForm()
    print(upload)
    if request.method == 'POST':
        upload = ProductForm(request.POST, request.FILES)
        mess = "Added successfully"
        return render(request,'adddesign.html',{'mess':mess,'upload_form':upload})
    else:
        return render(request, 'adddesign.html', {'upload_form':upload})