from django.shortcuts import render, redirect
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Character, Dialogue
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    

class About(TemplateView):
    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
class CharacterList(TemplateView):
    template_name = "character_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["characters"] = Character.objects.all()
        return context



class CharacterDetail(DetailView):
    model = Character
    template_name = "character_detail.html"

class DialogueCreate(View):

    def post(self, request, pk):
        quote = request.POST.get("quote")
        meaning = request.POST.get("meaning")
        character = Character.objects.get(pk=pk)
        Dialogue.objects.create(quote=quote, meaning=meaning, character=character)
        return redirect('character_detail', pk=pk)

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("character_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)



##############
#below was used for the lodal data before i switched to sql 
##############


# class Character:
#     def __init__(self, name, image, location):
#         self.name = name
#         self.image = image
#         self.location = location

# characters = [
#     Character("Cornifer", "https://static.wikia.nocookie.net/hollowknight/images/c/c1/Cornifer_Circle.png/revision/latest/scale-to-width-down/150?cb=20170426185850", "every area in the game"),
#     Character("Hornet", "https://static.wikia.nocookie.net/hollowknight/images/2/29/Hornet_Icon.png/revision/latest?cb=20170511203606", "Kingdoms Edge, Greenpath, the Abyss, City of Tears"),
#     Character("Zote", "https://static.wikia.nocookie.net/hollowknight/images/1/12/Zote_Circle-2.png/revision/latest?cb=20180831184143", "Dirtmouth, Colliseum of Fools, Deepnest, Greenpath"),
#     Character("Grimm", "https://static.wikia.nocookie.net/hollowknight/images/3/32/Grimm_Circle.png/revision/latest/scale-to-width-down/150?cb=20171029002401", "Dirtmouth")
# ]