from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home, name='Home'),
    path('blog/', views.blog, name='blog'),
    path('next/', views.next, name='next'),
    path('Add_post', views.Add_post, name='Add_post'),
    path('<slug:slug>/', views.detail, name='detail'),
]