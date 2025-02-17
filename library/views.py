from django.shortcuts import render, redirect
from django.views import generic
from .models import AddGame
from .forms import AddGameForm
from django.urls import reverse_lazy
from .bgg_api import fetch_bgg_game_data
from django.http import JsonResponse

# Create your views here.
def search_bgg_games(request):
    game_name = request.GET.get('game_name', '')
    if game_name:
        games = fetch_bgg_game_data(game_name)
        if games:
            return JsonResponse(games, safe=False)
    return JsonResponse({'error': 'No games found'}, status=404)

class GameDetailView(generic.DetailView):
    model = AddGame
    template_name = 'game_detail.html'
    context_object_name = 'game'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return AddGame.objects.filter(owner=self.request.user)
        else:
            return AddGame.objects.none()
        
class GamesList(generic.ListView):
    model = AddGame
    template_name = 'library.html'
    context_object_name = 'games_list'
    ordering = ['title']
    paginate_by = 6

    def get_queryset(self):
        queryset = AddGame.objects.none()
        if self.request.user.is_authenticated:
            queryset = AddGame.objects.filter(owner=self.request.user)
            min_players = self.request.GET.get('min_players')
            max_players = self.request.GET.get('max_players')
            if min_players:
                queryset = queryset.filter(minimum_player_count__gte=min_players)
            if max_players:
                queryset = queryset.filter(maximum_player_count__gte=max_players)
        return queryset
        
        
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