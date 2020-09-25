from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm, UploadForm
from django.utils import timezone

from main.models import Bar_code, Img
from .bar_read import bar_read
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    code_list = Bar_code.objects.order_by('-pub_date')[:]
    return render(request, 'home.html', {'code_list':code_list})

def product_detail(request, data_code):
    post = get_object_or_404(Bar_code, pk=data_code)
    return render(request, 'product_detail.html', {'post': post})



def upload_image(request):
    img_list = Img.objects.order_by('-pub_date')[:1]
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            imageURL = settings.MEDIA_URL + form.instance.image.name
            tmp = settings.MEDIA_ROOT_URL + imageURL
            post.save()
            if tmp:
                result = bar_read(tmp)
            return render(request, 'result.html', {'result':result})
    else:
        form = UploadForm()
    return render(request, 'upload_img.html', {'form':form, 'img_list':img_list})



def data_list(request):
    code_list = Bar_code.objects.order_by('-pub_date')[:]
    return render(request, 'data_list.html', {'code_list':code_list})

def data_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('/home/data_list')
    else:
        form = PostForm()
    return render(request, 'data_add.html', {'form': form})

def data_detail(request, data_code): 
    post = get_object_or_404(Bar_code, pk=data_code)
    return render(request, 'data_detail.html', {'post': post})

def data_update(request, data_code):
    post = get_object_or_404(Bar_code, pk=data_code)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('/home/data_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'data_add.html', {'form': form})

def data_delete(request, data_code):
    post = Bar_code.objects.get(pk=data_code)
    post.delete()
    return redirect('/home/data_list')

