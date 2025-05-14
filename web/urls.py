from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import MatchCreateView, MatchUpdateView, MatchDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('match/create/', MatchCreateView.as_view(), name='match-create'),
    path('match/<int:pk>/edit', MatchUpdateView.as_view(), name='match-edit'),
    path('match/<int:pk>/delete/', MatchDeleteView.as_view(), name='match-delete'),
    path('team/create/', TeamCreateView.as_view(), name='team-create'),
    path('team/<int:pk>/edit', TeamUpdateView.as_view(), name='team-edit'),
    path('team/<int:pk>/delete/', TeamDeleteView.as_view(), name='team-delete'),
    path('player/create/', PlayerCreateView.as_view(), name='player-create'),
    path('player/<int:pk>/edit', PlayerUpdateView.as_view(), name='player-edit'),
    path('player/<int:pk>/delete/', PlayerDeleteView.as_view(), name='player-delete'),

]