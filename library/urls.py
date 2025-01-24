from . import views
from django.urls import path
from django.conf import settings
from .views import GamesList, GameDeleteView, GameUpdateView, search_bgg_games, GameDetailView


urlpatterns = [ 
    path('', views.GamesList.as_view(), name='library'),
    path('search_bgg_games/', search_bgg_games, name='search_bgg_games'),
    path('delete/<int:pk>/', views.GameDeleteView.as_view(), name='game-delete'),
    path('update/<int:pk>/', views.GameUpdateView.as_view(), name='game-update'),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
]