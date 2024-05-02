from django.shortcuts import render, HttpResponseRedirect
from register_page.forms import UserForm
from django.contrib.auth.models import User as django_model_user
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Create your views here.

#To register a new user is better the use of the own django user model that provides several error exception at the time to fill the user's form.

def register(request):

    context = {}
    form = UserForm()

    if request.method == 'GET':
        context['form'] = form
        return render(request, "register_page.html", context)
    else:
        #Here we try to get the form info throught the method POST and we need to analyze than that information is valid to save it.
        try:
            #Password validation
            validate_password(request.POST['password'])
            if request.POST['password'] == request.POST['password_confirmation']:
                #New user creation validation
                try:
                    new_user = django_model_user.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                    new_user.save()
                    return HttpResponseRedirect("/login/")
                except:
                    return render(request, 'register_page.html', {'form': form, 'reg_error_user':f'El usuario ingresado no está disponible. Intenta con otro.'})
            else:
                return render(request, 'register_page.html', {'form':form, 'reg_error_password_match':'La confirmación de la contraseña no coincide. Intenta de nuevo.'}) 
        except ValidationError as e:
            print(f"Password error {e.messages}")
            return render(request, 'register_page.html', {'form':form, 'reg_error_password_val':'La contraseña debe tener al menos 8 carácteres, una mayúscula, una minúscula y un número'})     