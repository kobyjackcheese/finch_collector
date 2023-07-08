from django.urls import path, include
from . import views
from django.contrib import admin

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('characters/', views.CharacterList.as_view(), name="character_list"),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name="character_detail"),
    path('characters/<int:pk>/dialogues/new/', views.DialogueCreate.as_view(), name="dialogue_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]