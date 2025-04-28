from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import TeamCreateView, TeamUpdateView, TeamDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('teams/create/', TeamCreateView.as_view(), name='team-create'),
    path('teams/<int:pk>/edit', TeamUpdateView.as_view(), name='team-edit'),
    path('teams/<int:pk>/delete/', TeamDeleteView.as_view(), name='team-delete'),

] 