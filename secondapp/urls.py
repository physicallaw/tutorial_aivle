from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('army_shop/', views.army_shop),
    path('army_shop/<int:year>/<int:month>/', views.army_shop2),
    path('req/ajax/get/', views.ajaxGet),
    path('req/ajax/exam/', views.ajaxExam),
]