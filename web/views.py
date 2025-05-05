from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Match
from .forms import MatchForm
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
        equip = self.get_object()
        return self.request.user == equip.creador

class MatchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Match
    template_name = 'match_confirm_delete.html'
    success_url = reverse_lazy('teams')

    def test_func(self):
        equip = self.get_object()
        return self.request.user == equip.creador