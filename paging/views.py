from django.shortcuts import render
from secondapp.models import ArmyShop
from django.core.paginator import Paginator

def army_shop(request):
   now_page = int(request.GET.get('page', 1))
   datas = ArmyShop.objects.order_by('-id')
   p = Paginator(datas, 10)
   info = p.page(now_page)

   start_page = (now_page - 1) // 10 * 10 + 1
   end_page = start_page + 9
   if end_page > p.num_pages:
      end_page = p.num_pages

   context = {
      'info' : info,
      'page_range' : range(start_page, end_page + 1)
   }
   return render(request, 'paging/army_shop.html', context)