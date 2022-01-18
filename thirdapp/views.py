from django.shortcuts import render
from .models import Shop
def shop(request):
    shop_list = Shop.objects.all()
    return render(
        request,
        'thirdapp/shop.html',
        {'shop_list': shop_list}
    )