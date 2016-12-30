from django.shortcuts import render
from django.views import generic
from .models import Game

class IndexView(generic.ListView):
    template_name = 'gamification/index.html'
    context_object_name = 'game_list'
    
    def get_queryset(self):
        return Game.objects.all()
    
class RegisterView():
    pass

class LoginView():
    pass