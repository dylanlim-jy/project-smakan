from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('login', views.Login.as_view(), name='login'),
]
