from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
       #Get form values
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']

       #Check if password match
       if password == password2:
           #Check username
           if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken') 
                return redirect('register')
           else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is taken') 
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                    #Login after register
                    # auth.login(request, user)
                    # messages.success(request,'You are logged in')
                    # return redirect('index') 
                    user.save()
                    messages.success(request,'Account has been created') 
                    return redirect('login')
       else:
           messages.error(request,'Password do not match') 
           return redirect('register')   
    
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')