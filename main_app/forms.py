from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Payment, Subscription

sub_type = (('Free', 'Free'), ('Premium', 'Premium'))


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PaymentForm(forms.ModelForm):
    Card_number = forms.IntegerField(min_value=16, max_value=16)
    month = forms.IntegerField(min_value=2, max_value=2)
    year = forms.IntegerField(min_value=2, max_value=2)
    Security_code = forms.IntegerField(min_value=3, max_value=3)

    class Meta:
        model = Payment
        fields = ['First_name',
                  'Last_name',
                  'Card_number',
                  'month',
                  'year',
                  'Security_code']


class SubscriptionUpdateForm(forms.ModelForm):
    subscription = forms.CharField(widget=forms.RadioSelect(choices=sub_type))
    user = User.pk

    class Meta:
        model = Subscription
        fields = ['subscription']


class SubscriptionForm(forms.ModelForm):
    subscription = forms.CharField(widget=forms.RadioSelect(choices=sub_type))

    class Meta:
        model = Subscription
        fields = ['subscription']