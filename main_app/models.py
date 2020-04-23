from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

#User = settings.AUTH_USER_MODEL
sub_type = (('Free', 'Free'), ('Premium', 'Premium'))


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    subscription = models.CharField(max_length=30, default='Free', choices=sub_type)


class Payment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Card_number = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    Security_code = models.IntegerField()
