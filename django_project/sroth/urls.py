from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sroth-home'),
    path('apps/', views.sroth_apps, name='sroth-sroth_apps'),
    path('post/', views.post_view, name='sroth-post'),
    path('apps/<int:app_id>/', views.app_detail, name='app_detail'),
]
