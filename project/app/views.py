from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login ,logout as auth_logout ,authenticate
import random

from .forms import *
from .models import *

# Create your views here.


def login(request):
    if not request.user.is_authenticated():
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(phone=form.cleaned_data['phone'], password=form.cleaned_data['password'])
                if user is not None:
                    auth_login(request, user)
                    return redirect('index')
        else:
            form = LoginForm()
            form.auto_id = True
        return render(request,'account/login.html', {'form': form})
    else:
        return redirect('index')
    
def signup(request):
    if not request.user.is_authenticated():
        form=SignupForm()
        form.auto_id = True
        if request.method=="POST":
            form=SignupForm(request.POST)
            if form.is_valid():
                clean_password=form.cleaned_data
                lastname=clean_password.get('lastname')
                firstname=clean_password.get('firstname')
                password=clean_password.get('password')
                phone=clean_password.get('phone')
                user=Customuser.create_user(phone=phone,lastname=lastname,firstname=firstname)
                user.set_password(password)
                user.save()
                return redirect('index')
            else:
                return render(request,'account/signup.html', {'form': form})
        else:
            return render(request,'account/signup.html', {'form': form})
    else:
        return redirect('index')
    

def index(request):
    return render(request,'index.html')

def race(request):
    random_number=random.randint(1,10)
    quote=Quote.objects.filter(id=random_number).first()
    context={'quote': quote.to_dict()}
    return render(request,'race.html',context)

def handler404(request, exception):
    return render(request, '404.html', status=404)

