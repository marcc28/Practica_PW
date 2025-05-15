from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *

urlpatterns = [
    # Vistes principals
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('matches/', matchView, name='matches'),
    path('teams/', teamView, name='teams'),
    path('players/', playerView, name='players'),

    #Teams urls
    path('team/create/', TeamCreate, name='team-create'),
    path('teams/api/teams/', views.getTeams, name='getTeams'),
    path('team/<int:equipo_id>/edit', TeamUpdate, name='team-edit'),
    path('team/<int:equipo_id>/delete/', TeamDelete, name='team-delete'),

    # match urls
    path('match/create/', MatchCreate, name='match-create'),
    path('match/api/match/', views.getMatches, name='getMatch'),

    path('match/<int:match_id>/edit', MatchUpdate, name='match-edit'),
    path('match/<int:match_id>/delete/', MatchDelete, name='match-delete'),

    # players url
    path('player/create/', PlayerCreate, name='player-create'),
    path('player/api/players/', views.getPlayers, name='get-players'),
    path('player/<int:player_id>/edit', PlayerUpdate, name='player-edit'),
    path('player/<int:player_id>/delete/', PlayerDelete, name='player-delete'),
]
