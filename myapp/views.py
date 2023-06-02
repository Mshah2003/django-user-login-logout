from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('register')
        else:
            messages.info(request, 'password not same')
            return redirect('register')
    
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password = password)

        if user is not None:
            auth.login(request,user)
            return render(request, 'display.html',{'username':username})
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
        

    else:
        return render(request, 'login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('login')

def display(request):
    return render(request, 'display.html')