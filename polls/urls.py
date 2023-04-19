from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    # path('profile/<int:pk>',)
    path('about', views.AboutView.as_view(), name='about'),
    path('suggest', login_required(views.SuggestView.as_view()), name='suggest'),
    path('places', views.PlacesView.as_view(), name='places'),
]