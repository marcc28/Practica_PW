from django import forms
from .models import Match, Team, Player


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['home_team', 'away_team', 'utc_date', 'home_score', 'away_score', 'winner']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'tla', 'address', 'players']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name','nationality', 'position', 'shirt_number', 'current_team']