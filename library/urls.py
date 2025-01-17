from . import views
from django.urls import path

urlpatterns = [
    path('', views.LibraryList.as_view(), name='library'),
]