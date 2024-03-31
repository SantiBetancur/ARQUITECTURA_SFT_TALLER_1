from Login.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    return render(request,'login.html',{'title':'index'})


def Login(request):
    form = LoginForm
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['username']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')



        
    form = AuthenticationForm()
    return render(request, 'home.html', {'form':form, 'title':'log in'})
