from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from datetime import datetime

# Create your views here.
date=datetime.now().year

def home(request):
    current_date=datetime.now()

    context={
        'current_date':current_date,
        'date':date
    }
    return render(request,'myApp/home.html',context)

def register(request):
    if request.method == 'POST':
        # name = request.POST['name']
        # country=request.POST['country']
        username=request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            
            if User.objects.filter(email=email).exists():
                messages.success(request, f'{email} Is Already Exist')
                return redirect('register')
            elif User.objects.filter(username=user).exists():
                messages.success(request, f'{username} Is Already Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                # user.set_password(password)
                user.save()
            return redirect('log_in')
        else:
            messages.info(request, f'{username} your password not match!!!')
            return redirect('register')
    else:
        return render(request, 'myApp/register.html')

        
def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        if not User.objects.filter(username=username).exists():
            messages.info(request,"email is not found")
            return redirect('log_in')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"password is invalid")
            return redirect('log_in')

    return render(request,'myApp/login.html')


def log_out(request):
    logout(request)
    return redirect('log_in')

