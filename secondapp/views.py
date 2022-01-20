from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse('<u>Main</u>')

from .models import ArmyShop, Course
def insert(request):
    Course(name='데이터 분석', cnt=30).save()
    Course(name='데이터 수집', cnt=20).save()
    Course(name='웹개발', cnt=25).save()
    Course(name='인공지능', cnt=20).save()

    return HttpResponse('데이터 입력 완료')

def show(request):
    #          all() filter() get()
    c = Course.objects.all()
    # result = ''
    # for a in c:
    #     result += '%s %s<br>' % (a.name, a.cnt)

    # return HttpResponse(result)

    return render(
        request, 'secondapp/show.html',
        { 'data': c }
    )

def army_shop(request):
    # prd = request.GET.get('prd', '')  # 부작용 side effect
    prd = request.GET.get('prd')  # 부작용 side effect
    # prd = request.POST.get('prd')  # 부작용 side effect

    # shop = ArmyShop.objects.all()

    try:
        shop = ArmyShop.objects.filter(name__contains=prd)
    except:
        shop = ArmyShop.objects.all()

    ## Template Theme PlaceHolder
    return render(
        request, 
        'secondapp/army_shop.html',
        { 'data': shop }
    )

def army_shop2(request, year, month):
    shop = ArmyShop.objects.filter(year=year, month=month)
    
    # result = ''
    # for i in shop:    # formatting 방식 3가지
    #     result += '%s %s %s<br>' % (i.year, i.month, i.name)

    result = [ '%s %s %s<br>' % (i.year, i.month, i.name) for i in shop ]

    return HttpResponse(''.join(result))