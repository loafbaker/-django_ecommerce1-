from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate

# Create your views here.
from .forms import LoginForm, RegistrationForm

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    form = LoginForm(request.POST or None)
    submit_btn = 'Login'
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        user.emailconfirmed.active_user_email()

    context = {
        'form': form,
        'submit_btn': submit_btn,
    }
    return render(request, "form.html", context)

def registration_view(request):
    form = RegistrationForm(request.POST or None)
    submit_btn = 'Join'
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.save()
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # user = authenticate(username=username, password=password)
        # login(request, user)

    context = {
        'form': form,
        'submit_btn': submit_btn,
    }
    return render(request, "form.html", context)
