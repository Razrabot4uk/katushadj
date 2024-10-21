from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success_message, name='success_message'),
    path('announcements/', views.announcements_list, name='announcements_list'),
    
]
