from django.shortcuts import render
from django.views import generic
from .models import AddGame

# Create your views here.

class GamesList(generic.ListView):
    model = AddGame
    template_name = 'library.html'
    context_object_name = 'games_list'
    ordering = ['title']
    paginate_by = 5
    def get_queryset(self):
        return AddGame.objects.all()