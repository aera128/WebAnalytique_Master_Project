from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data1', views.data1, name='data1'),
    path('data2', views.data2, name='data2'),
]