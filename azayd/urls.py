from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('blog', views.blog, name='blog'),
    path('career', views.careers, name='careers'),
    path('sendRequest', views.sendRequest, name='sendRequest'),
]
