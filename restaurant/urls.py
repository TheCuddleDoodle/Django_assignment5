from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assign_staff/', views.assign_staff, name='assign_staff'),
    path('check_staff/', views.check_staff, name='check_staff'),
]