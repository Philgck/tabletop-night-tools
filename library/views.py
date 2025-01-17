from django.shortcuts import render
from django.views import generic
from .models import AddGame

# Create your views here.
class LibraryList(generic.ListView):
    queryset = AddGame.objects.all()
    template_name = "library/addgame_list.html"