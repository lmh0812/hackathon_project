from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import User
from django.utils import timezone

from user.models import MyUser
from django.conf import settings

# Create your views here.

def user_create(request):
    if request.method == "POST":
        form = User(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = User()
    return render(request, 'user_create.html', {'form': form})