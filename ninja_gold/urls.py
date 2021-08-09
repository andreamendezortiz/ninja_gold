from django.urls import path     
from . import views

urlpatterns = [
    path('ninja_gold', views.index),
    path('process_money', views.process_money),
    path('reset', views.reset),
]