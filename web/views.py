from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Match, Team, Player
from .forms import MatchForm, TeamForm, PlayerForm
import requests
# from .models import Book

# Create your views here.

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def matchView(request):
    return render(request, 'match.html')

def teamView(request):
    return render(request, 'team.html')

def playerView(request):
    return render(request, 'player.html')

def getTeams(request):
    headers = {
        #TODO: modificar token
        "X-Auth-Token" : "0ba4dbb5a5674096a1ae842cfe22366f"
    }
    url = "http://api.football-data.org/v4/competitions/PD/teams"
    response = requests.get(url, headers=headers)

    # Recuperar equips de la bse de datos
    equipos = list(Team.objects.values())



    if response.status_code == 200:
        datos = response.json()
        # Mezclar datos api amb base de datos
        for team in equipos:
            datos["teams"].append(team)

        # Retornar les dades
        return JsonResponse(datos)
    else:
        return JsonResponse({'error': 'No se pudo obtener la información'}, status=500)

class MatchCreateView(LoginRequiredMixin, CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'match_create.html'
    success_url = reverse_lazy('matches')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class MatchUpdateView(LoginRequiredMixin, UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'match_create.html'
    success_url = reverse_lazy('matches')

    def test_func(self):
        partit = self.get_object()
        return self.request.user == partit.creador

class MatchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Match
    template_name = 'match_confirm_delete.html'
    success_url = reverse_lazy('matches')

    def test_func(self):
        partit = self.get_object()
        return self.request.user == partit.creador

class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'team_create.html'
    success_url = reverse_lazy('teams')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'team_create.html'
    success_url = reverse_lazy('teams')

    def test_func(self):
        equip = self.get_object()
        return self.request.user == equip.creador

class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Team
    template_name = 'team_confirm_delete.html'
    success_url = reverse_lazy('teams')

    def test_func(self):
        equip = self.get_object()
        return self.request.user == equip.creador


class PlayerCreateView(LoginRequiredMixin, CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'player_create.html'
    success_url = reverse_lazy('players')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'player_create.html'
    success_url = reverse_lazy('players')

    def test_func(self):
        jugador = self.get_object()
        return self.request.user == jugador.creador

class PlayerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Player
    template_name = 'player_confirm_delete.html'
    success_url = reverse_lazy('players')

    def test_func(self):
        jugador = self.get_object()
        return self.request.user == jugador.creador