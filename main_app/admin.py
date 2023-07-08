from django.contrib import admin

# Register your models here.
from .models import Character # import the Artist model from models.py
from .models import Dialogue
# Register your models here.

admin.site.register(Character) # this line will add the model to the admin panel
admin.site.register(Dialogue)