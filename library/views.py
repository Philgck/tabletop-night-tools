from django.shortcuts import render, redirect
from django.views import generic
from .models import AddGame
from .forms import AddGameForm
from django.urls import reverse_lazy

# Create your views here.

class GamesList(generic.ListView):
    model = AddGame
    template_name = 'library.html'
    context_object_name = 'games_list'
    ordering = ['title']
    paginate_by = 6

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return AddGame.objects.filter(owner=self.request.user)
        else:
            return AddGame.objects.none()
        
        
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = AddGameForm(request.POST)
            if form.is_valid():
                new_game = form.save(commit=False)
                new_game.owner = request.user
                new_game.save()
                return redirect('library')
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['form'] = AddGameForm()
        return context
    
class GameDeleteView(generic.DeleteView):
    model = AddGame
    template_name = 'game_confirm_delete.html'
    success_url = reverse_lazy('library')

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return AddGame.objects.filter(owner=self.request.user)
        else:
            return AddGame.objects.none()