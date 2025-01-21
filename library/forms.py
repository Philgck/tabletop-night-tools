from django import forms
from .models import AddGame

class AddGameForm(forms.ModelForm):
    bgg_id = forms.CharField(max_length=100, required=False, label='BGG Game ID')

    class Meta:
        model = AddGame
        fields = ['title', 'description', 'review', 'minimum_player_count', 'maximum_player_count']