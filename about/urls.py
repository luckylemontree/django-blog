from . import views
from django.urls import path

urlpatterns = [
    path('', views.AboutList.as_view(), name='about'),
    path('<slug:slug>/', views.about_detail, name='about_detail'),
    
]