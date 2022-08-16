from django.urls import path
from mtweb import views

app_name='mtweb'
urlpatterns = [
    path('', views.index, name='index'),
]