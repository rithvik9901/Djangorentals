from django.db.models.query_utils import Q
from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models import customer
from store.models.customer import Customer
from django.views import  View
from django.views.decorators.csrf import csrf_exempt


class Login(View):
    return_url = None
    @csrf_exempt
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')

    @csrf_exempt
    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        flag = Customer.objects.filter(Q(email=email) & Q(password=password))
        if flag:
                request.session['customer'] = customer.id
                print(Login.return_url)
                print(type(Login.return_url))
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
        else:
            error_message = 'Email or Password invalid !!!!!!!!!'
        return render(request, 'login.html', {'error': error_message})
        





@csrf_exempt
def logout(request):
    request.session.clear()
    return redirect('login')
