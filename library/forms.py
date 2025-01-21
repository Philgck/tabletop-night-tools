from django import forms
from .models import AddGame

class AddGameForm(forms.ModelForm):
    class Meta:
        model = AddGame
        fields = ['title', 'description', 'minimum_player_count', 'maximum_player_count']