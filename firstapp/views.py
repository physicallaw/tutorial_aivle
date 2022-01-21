from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index1(request):
    return HttpResponse('<u>Hello</u><hr>Bye')

def index2(request):
    return HttpResponse('<u>Hi</u>')

def main(request):
    return HttpResponse('<u>Main</u>')

import firstapp.models as models
from .models import Curriculum

def insert(request):

    # 1  create()
    Curriculum.objects.create(name='linux')

    # 2  save()
    c = Curriculum(name='python')
    c.save()

    Curriculum(name='python').save()
    Curriculum(name='django').save()

    return HttpResponse('ok <h1>dkdkdkdkd</h1>')

def show(request):
    # curriculum = Curriculum.objects.all()
    # result = ''
    # for c in curriculum:
    #     result += c.name + '<br>'
    # return HttpResponse(result)

    #              필수!        필수! 변경가능    필수아님
    curriculum = Curriculum.objects.all()
    return render(
        request, 'show.html', 
        { 'score': 100, 'data': curriculum }
    )


def req_get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    result = '%s %s %s' % (a, b, c)
    return HttpResponse(result)

def req_post(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST['c']
        result = '%s %s %s' % (a, b, c)
        return HttpResponse(result)
    return render(request, 'firstapp/post.html')

def req_ajax4(request):
    return render(request, 'firstapp/ajax4.html')

import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def req_json(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)
    return JsonResponse(data)

def tag(request):
    persons = [
        { 'num': 1, 'name': 'Park', 'score': 100 },
        { 'num': 2, 'name': 'Choi', 'score': 70 },
        { 'num': 3, 'name': 'Kim', 'score': 80 }
    ]
    animals = ['Cat2', 'Dog']
    context = {
        'persons': persons,
        'animals': animals
    }
    return render(
        request, 'firstapp/tag.html', context)

def custom_filter(request):
    context = { 'price': 39800.5 }
    return render(
        request, 'firstapp/custom_filter.html', context)
    
def template(request):
    return render(
        request, 'firstapp/template.html')