from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('about', views.AboutView.as_view(), name='about'),
    path('suggest', views.SuggestView.as_view(), name='suggest'),
    path('places', views.PlacesView.as_view(), name='places'),
]
