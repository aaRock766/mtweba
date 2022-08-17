from django.urls import path
from mtweb import views

urlpatterns = [
    path('', views.index, name='index'),
]