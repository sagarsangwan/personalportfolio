from django.shortcuts import render
from .get_and_store_user_ip import get_client_ip_add, upload_user_ip, get_client_ip
# Create your views here.
import os


def home(request):
    if os.environ.get("MOD") == 'prod':
        ip = get_client_ip(request)
        upload_user_ip_add = upload_user_ip(ip, request)
    return render(request, 'pages/home.html')
