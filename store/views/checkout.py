from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from django.conf import settings
from django.core.mail import send_mail


class CheckOut(View):
    e = None
    a = None
    def post(self, request):
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)
        total=0
        print(total)
        for product in products:
            print(cart.get(str(product.id)))
            total = total +int(product.price)
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}
        print(total)
        '''
        subject = "Thank you for ordering the Products"
        message = "Your Delivery address : "+str(address) +"\nPayment paid :"+str(total)+ "\n \nYour Bank Details :\ndata here"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        context = {'data':total}
        '''
        request.session['e']=email
        request.session['a']=address
        request.session['total']=total
        return redirect('payment')
