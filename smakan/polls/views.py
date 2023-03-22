from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'polls/index.html')
