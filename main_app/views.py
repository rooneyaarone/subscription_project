from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm, PaymentForm, SubscriptionUpdateForm, SubscriptionForm
from .models import Subscription


def homepage(request):
    return render(request=request,
                  template_name='home.html')


def stream(request):
    return render(request=request,
                  template_name='stream.html')


def confirmation(request):
    return render(request=request,
                  template_name='confirmation.html')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            login(request, user)
            return redirect("main_app:subtype")
    else:
        form = UserRegistrationForm

    return render(request, "register.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, 'logged out successfully!')
    return redirect('main_app:homepage')


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'you are now logged in as {username}')
                return redirect('main_app:homepage')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()
    return render(request,
                  'login.html',
                  {'form': form})


def payment(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('main_app:confirmation')
    else:
        return render(request, 'payment.html', context={'form': form})


def subtype(request):
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        sub = form.cleaned_data.get('subscription')
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        if sub == 'Premium':
            return redirect('main_app:payment')
        else:
            return redirect('main_app:homepage')
    else:
        return render(request, 'subtype.html', context={'form': form})


def manage_account(request):
    return render(request=request,template_name='manage_account.html')






