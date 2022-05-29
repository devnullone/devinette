from django.contrib import admin

# Register your models here.

from .models import Level, Joueur, Devinette, Chiffre

admin.site.register(Level)
admin.site.register(Joueur)
admin.site.register(Devinette)
admin.site.register(Chiffre)