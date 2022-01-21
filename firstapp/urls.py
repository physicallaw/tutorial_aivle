from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('req/get/', views.req_get),
    path('req/post/', views.req_post),
    path('req/ajax4/', views.req_ajax4),
    path('req/json/', views.req_json),

    path('tag/', views.tag),
    path('custom_filter/', views.custom_filter),

    path('template/', views.template),
]