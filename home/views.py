from django.shortcuts import render
from .get_and_store_user_ip import get_client_ip_add, upload_user_ip
# Create your views here.


def home(request):
    ip = get_client_ip_add(request)
    print(ip)
    upload_user_ip_add = upload_user_ip(ip)
    print(upload_user_ip_add)
    return render(request, 'pages/home.html')
