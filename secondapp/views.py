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

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms.models import model_to_dict
@csrf_exempt
def ajaxGet(request):
    # QuerySet []
    c = Course.objects.all()
    
    data = []
    # model_to_dict - 조회된 데이터를 dict 형태로 변경
    for a in c:
        d = model_to_dict(a)
        data.append(d)

    return JsonResponse( data, safe=False )

def ajaxExam(request):
    return render( request, 'secondapp/ajax_exam.html' )

from django.shortcuts import redirect
from secondapp.forms import CourseForm
def course_create(request):
    if request.method == 'POST':
        ## form 미 사용시 작성되는 코드
        # name = request.POST.get('name')
        # cnt = request.POST.get('cnt')
        # c = Course(name=name, cnt=cnt)
        # c.save()

        # 1. 입력된 데이터를 한꺼번에 저장
        # 2. 유효성 검사 결과가 저장
        form = CourseForm( request.POST )
        if form.is_valid():
            # 데이터 저장
            course = form.save(commit=False)
            course.save()

            # 어딘가로 이동, 메시지 출력, ....
            return redirect('firstapp:post')
    else:
        form = CourseForm()

    return render(request, 'secondapp/course_create.html', {'form': form})