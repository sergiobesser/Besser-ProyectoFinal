from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login, authenticate
from .forms import MyUserForm


def accounts(request):
    return render(request, 'accounts/accounts.html', {})


def login_view(request):
    return render(request, 'accounts/login_view.html', {})


def login(request):
    msj = ''
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request, user)
                return redirect('login_view')
            else:
                msj= 'No se pudo autenticar el usuario'
        else:
            msj= 'El formulario no es valido'
    
    login_form = AuthenticationForm()
    return render(request, 'accounts/login_form.html', {'login_form': login_form, 'msj': msj})


def signup_view(request):
    return render(request, 'accounts/signup_view.html', {})


def signup(request):
    
    if request.method == 'POST':
        signup_form = MyUserForm(request.POST)
        
        if signup_form.is_valid():
            username = signup_form.cleaned_data['username']
            signup_form.save()
            return render(request, 'accounts/signup_view.html')
        else:
            return render(request, 'accounts/signup_form.html', {'signup_form': signup_form, 'msj': 'El formulario no es valido'})
        
    signup_form = MyUserForm()
    return render(request, 'accounts/signup_form.html', {'signup_form': signup_form})