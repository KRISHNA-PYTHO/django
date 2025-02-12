from django.urls import path
from .  import views

urlpatterns = [
    path('',views.index),
    path('formpost/',views.formpost),
    path('success/', views.success)
    ]