from django.contrib import admin
from .models import Match, Season, Team, Player

admin.site.register(Match)
admin.site.register(Season)
admin.site.register(Team)
admin.site.register(Player)