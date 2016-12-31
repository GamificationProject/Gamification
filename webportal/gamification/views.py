from django.shortcuts import render, redirect
from django.views import generic
from .models import Game
from .forms import UserForm
from django.views.generic import View
from django.contrib.auth import authenticate, login

class IndexView(generic.ListView):
    template_name = 'gamification/index.html'
    context_object_name = 'game_list'
    
    def get_queryset(self):
        return Game.objects.all()
    
class RegisterView(View):
    form_class = UserForm
    template_name = 'gamification/registration_form.html'
    
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleand_data['username']
            first_name = form.cleand_data['first_name']
            last_name = form.cleand_data['last_name']
            password = form.cleand_data['password']
            user.set_password(password)
            user.save()
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                if user.is_active():
                    login(request, user)
                    return redirect('gamification:index')
        
        return render(request, self.template_name, {'form': form})        

class LoginView(generic.FormView):
    pass