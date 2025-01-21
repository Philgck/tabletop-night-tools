from django.shortcuts import render, redirect
from django.views import generic
from .models import AddGame
from .forms import AddGameForm
from django.urls import reverse_lazy
from .bgg_api import fetch_bgg_game_data

# Create your views here.

def bgg_game_data(request, game_name):
    game_data = fetch_bgg_game_data(game_name)
    if game_data:
        return JsonResponse(game_data)
    else:
        return JsonResponse({'error': 'Game not found'}, status=404)

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
                bgg_id = form.cleaned_data.get('bgg_id')
                if bgg_id:
                    game_data = fetch_bgg_game_data(bgg_id)
                    if game_data:
                        form.instance.title = game_data['name']
                        form.instance.description = game_data['description']
                        form.instance.minimum_player_count = game_data['minplayers']
                        form.instance.maximum_player_count = game_data['maxplayers']
                        form.instance.image_url = game_data['image']
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
    
class GameUpdateView(generic.UpdateView):
    model = AddGame
    form_class = AddGameForm
    template_name = 'game_update_form.html'
    success_url = reverse_lazy('library')

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return AddGame.objects.filter(owner=self.request.user)
        else:
            return AddGame.objects.none()