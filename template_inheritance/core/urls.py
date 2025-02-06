from django.urls import path
from .  import views

urlpatterns = [
    path('',views.index),
    path('',views.about),
    path('',views.contact),
    path('',views.customer),
    path('',views.project)
    ]