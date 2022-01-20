from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home</h1>')

def text(request, char):
    return HttpResponse(char)

def date(request, year, month):
    return HttpResponse('%s - %s' % (year, month))

def search(request):
    title = request.GET.get('title')
    return HttpResponse('search : %s' % (title))

def info(request):
    id = request.GET.get('id')
    return HttpResponse('id : %s' % (id))

import os
def download(request, id):
    # 로그인 여부
    # ip 어떤 국가/지역
    # 블랙리스트
    filepath = 'c:/django/dog.jfif'
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response