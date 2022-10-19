from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from copeol_app import forms
def index (request):
    return render(request, "admin/base_site.html", context={'prenom': 'Moustapha'})

''' 
def login_page(request):
    message = ''
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'

            else:
                message = 'Login failed!'


    return render(request, "auth/login.html", context={'form': form, 'message': message})
 '''

# Login
def login_view(request):
    form = forms.LoginForm(request.POST or None)

    msg = None

    if not request.user.is_authenticated:
        if request.method == "POST":

            if form.is_valid():
                user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid credentials.')
            else:
                messages.error(request, 'Error validating the form.')
        return render(request, "auth/login.html", {"form": form, "msg": msg})
    return redirect("home")

# Dashboard
def home(request):
    if request.user.is_authenticated:
        return render(request, "home/home.html")
    return redirect('login')