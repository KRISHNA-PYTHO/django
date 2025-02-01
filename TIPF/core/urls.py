from django.urls import path
# from marvel import views
from core import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
]