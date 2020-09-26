from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm, UploadForm_Img, UploadForm_Code, Multi_Upload, ReviewForm
from django.utils import timezone

from main.models import Bar_code, Upload_Img, Upload_Code, Upload, Review
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
    review_list = Review.objects.order_by('-pub_date')[:]
    return render(request, 'product_detail.html', {'post': post, 'review_list': review_list})



def upload_image(request):
    if request.method == 'POST':
        form = UploadForm_Img(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            imageURL = settings.MEDIA_URL + form.instance.image.name
            tmp = settings.MEDIA_ROOT_URL + imageURL
            post.save()
            if tmp:
                result = bar_read(tmp)
                if result == Bar_code.objects.get(pk=result).pk:
                    return HttpResponseRedirect(reverse('main:product_detail',  args=(result,)))
    else:
        form = UploadForm_Img()
    return render(request, 'upload_img.html', {'form':form})

def upload_code(request):
    if request.method == 'POST':
        form = UploadForm_Code(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.pub_date = timezone.now()
            # post.save()
            result = post.title
            # try:
            if result == Bar_code.objects.get(pk=result).pk:
                return HttpResponseRedirect(reverse('main:product_detail',  args=(result,)))
            # except (KeyError, Choice.DoesNotExist):
            #     return render(request, 'upload_text.html', {'error_message': "Nothing DB",})
    else:
        form = UploadForm_Code()
    return render(request, 'upload_text.html', {'form':form})





def data_list(request):
    code_list = Bar_code.objects.order_by('-pub_date')[:]
    return render(request, 'data_list.html', {'code_list':code_list})

def data_add(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
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
        form = PostForm(request.POST, request.FILES, instance=post)
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





def result(request):
    if request.method == "POST":
        form = Multi_Upload(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        result = 0
        if form.is_valid():
            for f in files:
                file_instance = Upload(image=f)
                file_instance.save()   
                imageURL = settings.MEDIA_URL + str(f)
                tmp = settings.MEDIA_ROOT_URL + imageURL
                form.save()
                if tmp:
                    res = bar_read(tmp)
                    if res == Bar_code.objects.get(pk=res).pk:
                        result += Bar_code.objects.get(pk=res).charge
            return render(request, 'result.html', {'result': result})
    else:
        form = Multi_Upload()
    return render(request, 'upload_img.html', {'form': form})




def review(request, data_code):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        form.instance.code_name_id = Bar_code.objects.get(pk=data_code).pk
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
        return HttpResponseRedirect(reverse('main:product_detail', args=(data_code,)))
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})

 


def like(request, data_code):
    post = get_object_or_404(Bar_code, pk=data_code)
    return render(request, 'like.html', {'post': post})

def vote(request, data_code):
    post = get_object_or_404(Bar_code, pk=data_code)
    try:
        selected_choice = post.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'product_detail.html', {
            'post': post,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('main:like', args=(data_code,)))