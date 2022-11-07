from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('create', views.create, name='create'),
    path('about-us', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]