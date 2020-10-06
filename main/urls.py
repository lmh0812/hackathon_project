from django.contrib import admin
from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('home/<int:data_code>/', views.product_detail, name='product_detail'),

    path('home/upload_img/', views.upload_image, name='upload_image'),
    path('home/upload_code/', views.upload_code, name='upload_code'),


    path('home/data_list/', views.data_list, name='data_list'),
    path('home/data_add/', views.data_add, name='data_add'),
    path('home/data/<int:data_code>/', views.data_detail, name='data_detail'),
    path('home/<int:data_code>/update/', views.data_update, name='data_update'), 
    path('home/<int:data_code>/delete/', views.data_delete, name='data_delete'),
    path('home/result', views.result, name='result'),

    path('home/<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('home/<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:data_code>/like/', views.like, name='like'),
    path('<int:data_code>/vote/', views.vote, name='vote'),

    path('home/introduce/', views.introduce, name='introduce'),

    path('home/cal_result', views.cal_result, name='cal_result'),
]
