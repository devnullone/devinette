from . import views
from django.urls import path

app_name = 'game'

urlpatterns = [
    path('home', views.demarrage, name="demarage"),
    path('pseudo', views.pseudo, name="pseudo"),
    path('mot', views.getdevinettemot, name="devinette_mot"),
    path('chiffre', views.getdevinetteChiffre, name="devinette_chiffre"),
    #path('<slug:category_slug>/', views.category, name="category"),

]
