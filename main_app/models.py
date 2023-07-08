from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Character(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    location = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Dialogue(models.Model):

    quote = models.CharField(max_length=300)
    meaning = models.CharField(max_length=300)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="dialogues")

    def __str__(self):
        return self.quote
