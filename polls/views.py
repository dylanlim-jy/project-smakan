from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'polls/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add recent events filter
        return context
    
class Login(LoginView):
    template_name = 'polls/login.html'
    def get(self, *args, **kwargs):
        return

class AboutView(TemplateView):
    pass

# @login_required - add this on the urls by wrapping this view func in the wrapper - eg login_required(SuggestView.as_view())
class SuggestView(TemplateView):
    pass

class AddPlace(TemplateView):
    pass