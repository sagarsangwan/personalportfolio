
from urllib import request
from .models import UserIpAddress


PRIVATE_IPS_PREFIX = ('10.', '172.', '192.', )


def get_client_ip(request):
    """get the client ip from the request
    """
    remote_address = request.META.get('REMOTE_ADDR')
    # set the default value of the ip to be the REMOTE_ADDR if available
    # else None
    ip = remote_address
    # try to get the first non-proxy ip (not a private ip) from the
    # HTTP_X_FORWARDED_FOR
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        proxies = x_forwarded_for.split(',')
        # remove the private ips from the beginning
        while (len(proxies) > 0 and
                proxies[0].startswith(PRIVATE_IPS_PREFIX)):
            proxies.pop(0)
        # take the first ip which is not a private one (of a proxy)
        if len(proxies) > 0:
            ip = proxies[0]

    return ip


def get_client_ip_add(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def upload_user_ip(ip, request):
    if UserIpAddress.objects.filter(user_ip=ip).exists():
        current_user = UserIpAddress.objects.get(user_ip=ip)
        current_user.times_user_viewed += 1
        current_user.save()
        return "added successfully old user"
    else:
        ip_without_proxy = get_client_ip(request)
        UserIpAddress.objects.create(
            user_ip=ip_without_proxy,
            times_user_viewed=1,
            user_ip_without_proxy=ip)
        return "added successfully new user and ip is {} and ip without proxy is {}".format(ip, ip_without_proxy)
