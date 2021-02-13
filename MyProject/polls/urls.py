from django.urls import path
from  .views import  HelloWorldView

urlpatterns = [
    path('',HelloWorldView,name='home'),
]