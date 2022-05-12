from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from django.conf import settings
from django.core.mail import send_mail

class Payment(View):
    @csrf_exempt
    def get(self,request):
        total=request.session.get('total')
        return render(request,'payment.html',{'total':total})

    @csrf_exempt
    def post(self,request):
        aname = request.POST['aname']
        anum = request.POST['anum']
        exdate = request.POST['exdate']
        cvv = request.POST['cvv']
        print(aname)
        a=request.session.get('a')
        e=request.session.get('e')
        total=request.session.get('total')
        subject = "Thank you for ordering the Products"
        message = "From Wagen Rentals :\n\n You have placed a order in Wagen Rentals H \nYour Delivery address : "+str(a) +"\nPayment paid :"+str(total)+ "\n \nYour Bank Details :\n\nAccount Holder Name :"+str(aname)+"\nAccount Number :"+str(anum)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('orders')