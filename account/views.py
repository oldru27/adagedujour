from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def creercompte(request):
    if request.method == 'POST':
        print('yopost')
        if request.POST['password'] == request.POST['confirmpassword']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render (request,'account/signup.html', {'iferrors':'Username deja pris'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request,user)
                return redirect('maison')
        else:         #faire le signup
            return render(request, 'account/signup.html', {'iferrors': 'Mettre deux password identique'})
    else:  # faire le signup
        print('yoget')
        return render(request, 'account/signup.html')


def selogger(request):
    return render(request,'account/signin.html')

def sedeco(request):
    return render(request,'account/signup.html')