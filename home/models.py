# from email.policy import default
# from ipaddress import ip_address
from django.db import models

# Create your models here.

# from .get_and_store_user_ip import get_client_ip_add, upload_user_ip, get_client_ip


class UserIpAddress(models.Model):
    user_ip = models.CharField(max_length=100)
    user_ip_without_proxy = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    times_user_viewed = models.IntegerField(default=0)

    def __str__(self):
        return self.user_ip


class Contactme(models.Model):
    user_ip_address = models.ForeignKey(
        UserIpAddress, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name:
            return self.name
        elif self.email:
            return self.email
        else:
            return self.message

        # super().save(*args, **kwargs)
