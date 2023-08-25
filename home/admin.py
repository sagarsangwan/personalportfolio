from django.contrib import admin

# Register your models here.
from .models import UserIpAddress, Contactme

admin.site.register(UserIpAddress)

admin.site.register(Contactme)
