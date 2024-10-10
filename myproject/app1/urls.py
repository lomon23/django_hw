from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_app1, name='hello_app1'),
]