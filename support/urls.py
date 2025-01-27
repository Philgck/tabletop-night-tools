from django.urls import path
from . import views

urlpatterns = [
    path('', views.support, name='support'),
    path('thanks/', views.support_thanks, name='support_thanks'),
]