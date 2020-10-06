from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import PostForm, UploadForm_Img, UploadForm_Code, Multi_Upload, ReviewForm
from django.utils import timezone

from main.models import Bar_code, Upload_Img, Upload_Code, Upload, Review, Choice
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
        bar_list = []
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
                        bar_list.append("코드: " + str(Bar_code.objects.get(pk=res).code) +" \t상품명: "+ Bar_code.objects.get(pk=res).name +" \t가격: "+ str(Bar_code.objects.get(pk=res).charge))
            return render(request, 'result.html', {'result': result, 'bar_list':bar_list})
    else:
        form = Multi_Upload()
    return render(request, 'upload_img_total.html', {'form': form})





def comments_create(request, post_id):
    post = Bar_code.objects.get(pk=post_id).pk
    content = request.POST.get('content')
    comment = Review(code_name_id=int(post), review_text=content)
    comment.save()

    return HttpResponseRedirect(reverse('main:product_detail', args=(post_id,)))

def comments_delete(request, post_id, comment_id):
    comment = Review.objects.get(pk=comment_id)
    comment.delete()
    
    return HttpResponseRedirect(reverse('main:product_detail', args=(post_id,)))



 


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
        return HttpResponseRedirect(reverse('main:product_detail', args=(data_code,)))

def introduce(request):
    return render(request,'introduce.html')

def cal_result(request):
    if request.method == "POST":
        form = Multi_Upload(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        result1 = 0
        result2 = 0
        result3 = 0
        result4 = 0
        result5 = 0
        bar_list = []
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
                        result1 += Bar_code.objects.get(pk=res).total
                        result2 += Bar_code.objects.get(pk=res).kcal
                        result3 += Bar_code.objects.get(pk=res).carbo
                        result4 += Bar_code.objects.get(pk=res).protein
                        result5 += Bar_code.objects.get(pk=res).fat
                        bar_list.append("총 제공량 : " + str(Bar_code.objects.get(pk=res).total)+"g" 
                        +" \t열량: "+ str(Bar_code.objects.get(pk=res).kcal)+"g" 
                        +" \t탄수화물: "+ str(Bar_code.objects.get(pk=res).carbo)+"g"
                        +" \t단백질: "+ str(Bar_code.objects.get(pk=res).protein)+"g"
                        +" \t지방: "+ str(Bar_code.objects.get(pk=res).fat)+"g")
            return render(request, 'cal_result.html', {'result1': result1, 'result2': result2, 'result3': result3, 'result4': result4, 'result5': result5, 'bar_list':bar_list})
    else:
        form = Multi_Upload()
    return render(request, 'upload_img_cal.html', {'form': form})