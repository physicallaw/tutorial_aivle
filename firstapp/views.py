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

    return HttpResponse('ok')