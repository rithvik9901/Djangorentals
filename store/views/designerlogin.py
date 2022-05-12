from store.models import Designer
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.hashers import  check_password

from django.views import  View

class Designer(View):
    def get(self,request):
        return render(request,'designerlogin.html')

    def post(self, request):
        mail = request.POST['un']
        pwd = request.POST['pw']
        arr = {"30259":"wagen","30226":"password","30259":"password"}
        if mail in arr:
            if arr[mail] == pwd:
                flag=True
            else:
                flag=False
        else:
            flag=False
        if flag:
            request.session['email'] = mail
            data = mail
            print("after setting: " + data)
            if data != None:
                return render(request, 'designhome.html', {'data': data})
            else:
                return HttpResponse('Session variable none')
        else:
            return HttpResponse("invalid")

    def home(request):
        data = request.session.get('email')
        return render(request,'designhome.html',{'data':data})

    def addreq(request):
        return render(request,'Requestadesign.html')

def deslogout(request):
    request.session.clear()
    return render(request,'designerlogin.html')

    