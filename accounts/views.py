import email
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login, authenticate
from .forms import MyUserForm, EditForm
from django.contrib.auth.decorators import login_required
from .models import UserExtension


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


@login_required
def edit(request):
    
    user_extension_logued, _ = UserExtension.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        edit_form = EditForm(request.POST, request.FILES)
        
        if edit_form.is_valid():
            request.user.first_name = edit_form.cleaned_data['first_name']
            request.user.last_name = edit_form.cleaned_data['last_name']
            request.user.email = edit_form.cleaned_data['email']
            user_extension_logued.avatar = edit_form.cleaned_data['avatar']
            user_extension_logued.link = edit_form.cleaned_data['link']
            user_extension_logued.more_description = edit_form.cleaned_data['more_description']
            
            if edit_form.cleaned_data['password1'] != '' and edit_form.cleaned_data['password1'] == edit_form.cleaned_data['password2']:
                request.user.set_password(edit_form.cleaned_data['password1'])
            
            request.user.save()
            user_extension_logued.save()
            
            return redirect('index')
        else:
            return render(request, 'accounts/edit_user.html', {'edit_form': edit_form, 'msj': 'El formulario no es valido'})
        
    edit_form = EditForm(
        initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,            
            'password1': '',
            'password2': '',
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
            'more_description': user_extension_logued.more_description
        }
    )
    return render(request, 'accounts/edit_user.html', {'edit_form': edit_form})


@login_required
def profile(request):
    user_extension, _ = UserExtension.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'user_extension': user_extension})
    
    