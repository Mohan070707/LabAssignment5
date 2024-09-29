from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world_json, name='hello_world_json'),
]
