from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .models import User

class HomeView(TemplateView):
    template_name = 'polls/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add recent events filter
        return context
    
class Login(LoginView):
    template_name = 'polls/login.html'
    redirect_authenticated_user = True

class Logout(LogoutView):
    next_page = 'polls:login'
    
class RegisterView(CreateView):
    template_name_suffix = '_create_form'
    model = User
    fields = ['email', 'username', 'pin']
    
    def get_success_url(self):
        return reverse('polls:index'
                    #    , kwargs={'username': self.object.username}
                       )

class AboutView(TemplateView):
    template_name = 'polls/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# @login_required - add this on the urls by wrapping this view func in the wrapper - eg login_required(SuggestView.as_view())
class SuggestView(TemplateView):
    template_name = 'polls/suggest.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PlacesView(TemplateView):
    template_name = 'polls/places.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context