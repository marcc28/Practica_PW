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
import json


# from .models import Book

# Create your views here.

def home(request):
    headers = {
        "X-Auth-Token": "0ba4dbb5a5674096a1ae842cfe22366f"
    }

    standings_url = "https://api.football-data.org/v4/competitions/PD/standings"
    scorers_url = "https://api.football-data.org/v4/competitions/PD/scorers"

    standings = []
    scorers = []

    try:
        res_standings = requests.get(standings_url, headers=headers)
        res_scorers = requests.get(scorers_url, headers=headers)
        if res_standings.status_code == 200:
            standings = res_standings.json()["standings"][0]["table"]
        if res_scorers.status_code == 200:
            scorers = res_scorers.json()["scorers"]
    except Exception as e:
        print("Error calling API:", e)

    return render(request, "home.html", {
        "standings": standings,
        "scorers": scorers
    })


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
    teams = Team.objects.all()
    return render(request, 'player.html', {'teams': teams})


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
        return JsonResponse({'error': str(e)}, status=500)


def getTeams(request):
    equipos = fetch_all_teams()
    return JsonResponse(equipos, safe=False)


def TeamUpdate(request, equipo_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)

            equipo = Team.objects.get(id=equipo_id)
            equipo.name = data.get('name', equipo.name)
            equipo.founded = data.get('founded', equipo.founded)
            equipo.venue = data.get('venue', equipo.venue)
            equipo.coach = data.get('coach', equipo.coach)
            equipo.crest = data.get('crest', equipo.crest)
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
            return JsonResponse({"mensaje": "Equipo eliminado"}, status=201)
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Equipo no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


def MatchCreate(request):
    pass


def getMatches(request):
    headers = {
        "X-Auth-Token": "0ba4dbb5a5674096a1ae842cfe22366f"
    }
    url = "http://api.football-data.org/v4/competitions/PD/matches"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        datos = response.json()
        return JsonResponse(datos["matches"], safe=False)
    else:
        return JsonResponse({'error': 'No se pudo obtener la información'}, status=500)


def getMatchById(request, match_id):
    headers = {
        "X-Auth-Token": "0ba4dbb5a5674096a1ae842cfe22366f"
    }
    url = "http://api.football-data.org/v4/matches/"
    url += str(match_id)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        datos = response.json()
        return JsonResponse(datos, safe=False)
    else:
        return JsonResponse({"mensjae": "error recuperando los datos de la api"}, status=500)


def MatchUpdate(request, equipo_id):
    pass


def MatchDelete(request, equipo_id):
    pass


def PlayerCreate(request):
    try:
        data = json.loads(request.body)
        name = data.get('name')
        nationality = data.get('nationality')
        position = data.get('position')
        birth_date = data.get('birth_date')
        team_id = data.get('team')

        if not name or not nationality or not position or not birth_date or not team_id:
            return JsonResponse({'error': 'missing atributes'}, status=400)

        team = Team.objects.get(id=int(team_id))

        player = Player.objects.create(
            name=name,
            nationality=nationality,
            position=position,
            date_of_birth=birth_date,
            current_team=team,
            creador=request.user,
        )

        return JsonResponse({
            'name': player.name,
            'nationality': player.nationality,
            'position': player.position
        }, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'inavlid JSON'}, status=400)
    except Team.DoesNotExist:
        print("team does not exist")
        return JsonResponse({'error': 'Invalid team'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def getPlayers(request):
    players = []
    teams = fetch_all_teams()
    for team in teams:
        squad = team["squad"]

        if ("creador" not in team):
            teamName = team["name"]
            crest = team["crest"]
            for player in squad:
                player["team"] = teamName
                player["crest"] = crest
        players.extend(squad)
    # Retornar les dades
    return JsonResponse(players, safe=False)


def PlayerUpdate(request, player_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            print(data, player_id)
            player = Player.objects.get(id=player_id)
            player.name = data.get('name', player.name)
            player.nationality = data.get('nationality', player.nationality)
            player.position = data.get('position', player.position)
            player.date_of_birth = data.get('birth_date', player.date_of_birth)
            team_id = data.get('team')

            if team_id:
                team = Team.objects.get(id=int(team_id))
                player.current_team = team

            player.save()

            return JsonResponse({"mensaje": "Player updated"}, status=201)
        except Player.DoesNotExist:
            return JsonResponse({'error': 'Player no encontrado'}, status=404)
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Equipo no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


def PlayerDelete(request, player_id):
    if request.method == "DELETE":
        try:
            player = Player.objects.get(id=player_id)
            player.delete()
            return JsonResponse({"mensaje": "Player eliminado"}, status=201)
        except Player.DoesNotExist:
            return JsonResponse({'error': 'Player not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


def fetch_all_teams():
    headers = {
        "X-Auth-Token": "0ba4dbb5a5674096a1ae842cfe22366f"
    }
    url = "http://api.football-data.org/v4/competitions/PD/teams"
    response = requests.get(url, headers=headers)

    equipos = Team.objects.prefetch_related('squad').all()

    equipos_serializados = []
    for equipo in equipos:
        equipos_serializados.append({
            'id': equipo.id,
            'name': equipo.name,
            'crest': equipo.crest,
            'founded': equipo.founded,
            'venue': equipo.venue,
            "creador_id": equipo.creador_id,
            'coach': equipo.coach,
            'squad': [
                {
                    'id': jugador.id,
                    'name': jugador.name,
                    'nationality': jugador.nationality,
                    'position': jugador.position,
                    'birth_date': jugador.date_of_birth,
                    'creator_id': jugador.creador.id,
                    "team_id": jugador.current_team.id
                } for jugador in equipo.squad.all()
            ]
        })
    equipos_api = []
    if response.status_code == 200:
        datos = response.json()
        equipos_api = datos.get("teams", [])

    return equipos_serializados + equipos_api


def team_detail_page(request, pk):
    headers = {
        "X-Auth-Token": "0ba4dbb5a5674096a1ae842cfe22366f"
    }
    api_url = f"https://api.football-data.org/v4/teams/{pk}"
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        team = response.json()
        return render(request, 'team_detail.html', {'team': team})
    else:
        return render(request, 'team_detail.html', {'error': 'Team not found'})