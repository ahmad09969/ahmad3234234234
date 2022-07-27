from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_login , name = 'show_login' ) ,
    path('logup/', views.show_logup , name = 'show_logup' ) ,
]
