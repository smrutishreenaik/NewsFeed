from . import views
from django.urls import path

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('create/', views.news_create, name='news_create'),
    path('<int:news_id>/edit/', views.news_edit, name='news_edit'),
    path('<int:news_id>/delete/', views.news_delete, name='news_delete'),
    path('register/', views.register, name='register'),
] 
