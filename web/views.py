from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Match, Team, Player
from .forms import MatchForm, TeamForm, PlayerForm
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