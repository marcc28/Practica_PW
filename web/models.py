from django.contrib.auth.models import User
from django.db import models


# Modelo de Player
class Player(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    shirt_number = models.IntegerField()
    last_updated = models.DateTimeField()
    current_team = models.ForeignKey('Team', related_name='current_players', on_delete=models.CASCADE, null=True, blank=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Modelo de Team
class Team(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50, null=True, blank=True)
    tla = models.CharField(max_length=10, null=True, blank=True)  # Three-letter abbreviation
    crest = models.URLField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    founded = models.IntegerField(null=True, blank=True)
    club_colors = models.CharField(max_length=100, null=True, blank=True)
    venue = models.CharField(max_length=100, null=True, blank=True)
    players = models.ManyToManyField(Player)  # Relación de muchos a muchos con Player
    creador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Modelo de Match
class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    competition = models.CharField(max_length=100)  # Nombre de la competencia, por ejemplo "FIFA World Cup"
    season = models.CharField(max_length=100)  # Temporada del partido
    utc_date = models.DateTimeField()  # Fecha y hora en UTC del partido
    venue = models.CharField(max_length=100)
    status = models.CharField(max_length=50)  # "TIMED", "FINISHED", etc.
    home_score = models.IntegerField(null=True, blank=True)  # Resultado de goles para el equipo local
    away_score = models.IntegerField(null=True, blank=True)  # Resultado de goles para el equipo visitante
    winner = models.CharField(max_length=50, null=True, blank=True)  # "home", "away", o "draw"
    creador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.home_team.name} vs {self.away_team.name}'

