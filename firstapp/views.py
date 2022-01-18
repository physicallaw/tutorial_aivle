from django.shortcuts import render
from django.http import HttpResponse

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