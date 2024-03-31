from Login.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login

# Create your views here.

def Login(request):
    form = LoginForm()
    if request.method == 'GET':
        return render (request, 'Login.html', {'form':form})
    else:
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate user with Django
        user = authenticate(request, username = username, password = password)

        try:
            if(user is not None):
                #Login user in the database
                print(f'User: {username} is log in')
                login(request, user)
                return redirect("/available_communities/")
            else:
                return render(request, 'Login.html',{'form':form, 'log_error_user':'Nombre de usuario o contraseña incorrectos.'})
        except:
            return render(request, 'Login.html',{'form':form, 'log_error_user':'Nombre de usuario o contraseña incorrectos.'})