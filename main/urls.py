from django.contrib import admin
from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('home/<int:data_code>/', views.product_detail, name='product_detail'),

    path('home/upload_img/', views.upload_image, name='upload_image'),

    path('home/data_list/', views.data_list, name='data_list'),
    path('home/data_add/', views.data_add, name='data_add'),
    path('home/data/<int:data_code>/', views.data_detail, name='data_detail'),
    path('home/<int:data_code>/update/', views.data_update, name='data_update'), 
    path('home/<int:data_code>/delete/', views.data_delete, name='data_delete'),

]
