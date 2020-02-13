from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, LoginForm

# Create your views here.

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            # If form not valid, redirect user's errors to context
            context['registration_form'] = form
    else:
        # If not post request, then let user see an empty form
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "account/register.html", context)

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('index')

    if request.POST:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                # Unsuccessfull login, redirect error to context
                context['login_form'] = form
        else:
            # If form not valid, redirect user's errors to context
            context['login_form'] = form
    else:
        # If not post request, then let user see an empty form
        form = LoginForm()
        context['login_form'] = form
    return render(request, "account/login.html", context)

def logout_view(request):
    logout(request)
    return redirect('index')

