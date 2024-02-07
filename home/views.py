from django.shortcuts import render
from .get_and_store_user_ip import get_client_ip_add, upload_user_ip, get_client_ip

# Create your views here.
import os
from .forms import ContactMeForm
from .models import Contactme, UserIpAddress
from django.http import JsonResponse
import json


def home(request):
    form = ContactMeForm()
    # if os.environ.get("MOD") == "prod":
    ip = get_client_ip(request)
    # upload_user_ip_add = upload_user_ip(ip, request)
    context = {"form": form}
    return render(request, "pages/home.html", context)


def contact_me(request):
    if request.method == "POST":
        bdata = json.loads(request.body)
        name = bdata.get("name")
        email = bdata.get("email")
        message = bdata.get("message")
        if name and email and message:
            new_message = Contactme(
                name=bdata.get("name"),
                email=bdata.get("email"),
                message=bdata.get("message"),
            )
            new_message.save()

            data = {"name": name, "email": email, "message": message}
            print(data)
            return JsonResponse(data, safe=False)
        error = ""
        if not name:
            error = "enter name correctly"
        elif not email:
            error = "enter email correctly"
        else:
            error = "enter message correctly"
        return JsonResponse({"error": error}, status=500)
        # c_user = get_client_ip(request)
        # if UserIpAddress.objects.filter(user_ip=c_user).exists():
        #     c_user = UserIpAddress.objects.get(user_ip=c_user)

        #
        # print(bdata.get("name"))
        # if name and email and message:
        #
        # new_message.save()
        # data = {"name": name, "email": email, "message": message}
        # print(data)
        # return JsonResponse(data, safe=False)

        # return JsonResponse({"error": ""}, status=500)

    #     if UserIpAddress.objects.filter(user_ip=c_user).exists():
    #         c_user = UserIpAddress.objects.get(user_ip=c_user)
    #         print(c_user, "exists")
    #     form = ContactMeForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         form.instance.user_ip_address = c_user
    #         form.save()
    #         print(form)
    #         return JsonResponse({"success": "true"})
    #     else:
    #         print(form.errors)
    #         return JsonResponse({"error": form.errors}, status=400)
    # else:
    #     return JsonResponse({"error": ""}, status=400)
