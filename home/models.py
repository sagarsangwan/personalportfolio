from email.policy import default
from ipaddress import ip_address
from django.db import models

# Create your models here.


class UserIpAddress(models.Model):
    user_ip = models.CharField(max_length=100)
    user_ip_without_proxy = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    times_user_viewed = models.IntegerField(default=0)

    def __str__(self):
        return self.user_ip
