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
import  json
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

def TeamCreate(request):
    try:
        data = json.loads(request.body)  # parsea JSON enviado en body
        nombre = data.get('name')
        crest = data.get('crest')
        founded = data.get('founded')
        venue = data.get('venue')
        coach = data.get('coach')

        if not nombre:
            return JsonResponse({'error': 'El nombre es obligatorio'}, status=400)

        # Crear equipo
        team = Team.objects.create(
            name=nombre,
            crest=crest,
            founded=founded,
            venue=venue,
            coach=coach,
            creador=request.user,
        )

        return JsonResponse({
            'name': team.name,
            'crest': team.crest,
            'founded': team.founded,
            'venue': team.venue,
            'coach': team.coach,
        }, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    except Exception as e:
        print("hay error jente")
        return JsonResponse({'error': str(e)}, status=500)

def getTeams(request):
    headers = {
        #TODO: modificar token
        "X-Auth-Token" : "0ba4dbb5a5674096a1ae842cfe22366f"
    }
    url = "http://api.football-data.org/v4/competitions/PD/teams"
    response = requests.get(url, headers=headers)

    equipos = Team.objects.prefetch_related('players').all()

    equipos_serializados = []
    for equipo in equipos:
        equipos_serializados.append({
            'id': equipo.id,
            'name': equipo.name,
            'crest': equipo.crest,
            'founded': equipo.founded,
            'venue': equipo.venue,
            "creador_id": equipo.creador_id,
            'coach': {'name': equipo.coach} if hasattr(equipo, 'coach_name') else {},
            'jugadores': [
                {
                    'id': jugador.id,
                    'nombre': jugador.name,
                    'nacionalidad': jugador.nationality
                } for jugador in equipo.players.all()
            ]
        })

    print(equipos_serializados)

    if response.status_code == 200:
        datos = response.json()
        # Mezclar datos api amb base de datos
        datos["teams"].extend(equipos_serializados)

        # Retornar les dades
        return JsonResponse(datos)
    else:
        return JsonResponse({'error': 'No se pudo obtener la información'}, status=500)



def TeamUpdate(request, equipo_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)

            equipo = Team.objects.get(id=equipo_id)
            equipo.name = data.get('name', equipo.name)
            equipo.founded = data.get('founded', equipo.founded)
            equipo.venue = data.get('venue', equipo.venue)
            equipo.save()

            return JsonResponse({'mensaje': 'Equipo actualizado con éxito'})
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Equipo no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def TeamDelete(request, equipo_id):
    if request.method == "DELETE":
        try:
            equipo = Team.objects.get(id=equipo_id)
            equipo.delete()
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Equipo no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def MatchCreate(request):
    pass

def getMatches(request):
    pass

def MatchUpdate(request, equipo_id):
    pass

def MatchDelete(request, equipo_id):
    pass


def PlayerCreate(request):
    pass

def getPlayers(request):
    pass

def PlayerUpdate(request, equipo_id):
    pass

def PlayerDelete(request, equipo_id):
    pass
