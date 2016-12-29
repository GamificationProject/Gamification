from django.contrib import admin
from .models import Game

class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['game_name']}),
        ('Description', {'fields': ['game_description']})
    ]
    
admin.site.register(Game, GameAdmin)    
