from django.shortcuts import render , redirect , HttpResponseRedirect

from store.models.customer import Customer
from django.views import  View
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add(request):
    if request.method == 'POST':
        key = request.session.get('customer')
        a=Customer.objects.get(id=key)
        fn=request.POST['fn']
        ln=request.POST['ln']
        email=request.POST['email']
        pw=request.POST['pass']
        add=True
        if fn != "":
            a.first_name=fn
        if ln != "":
            a.last_name=ln
        if pw != "":
            a.phone = pw
        if email != "":
            a.email = email
        a.save()
        print(fn)
        return redirect('myprofile')
    else:
        key = request.session.get('customer')
        print(type(id))
        form = Customer.objects.all()
        print(form)
        return render(request,'myprofile.html',{'form':form,'key':key})

@csrf_exempt
def updpass(request):
    if request.method == 'POST':
        key = request.session.get('customer')
        print("inside")
        a=Customer.objects.get(id=key)
        np=request.POST['con']
        a.password = np
        a.save()
        return redirect('myprofile')
    else:
        return redirect('myprofile')

def deleteacc(request):
    key = request.session.get('customer')
    a=Customer.objects.get(id=key)
    request.session.clear()
    a.delete()
    return redirect('deletepage')

def delpage(request):
    return render(request,'deletepage.html')
