from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# Register your models here.
admin.site.site_header = 'THCP ADMINISTRATION'

admin.site.register(contactUs)
admin.site.register(categories)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)

# Mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "first_name", "last_name", "email"]  # Utilisation de 'fields' au lieu de 'field'
    inlines = [ProfileInline]

# Unregister the old way
admin.site.unregister(User)

# Re-Register the new way
admin.site.register(User, UserAdmin)

# Configuration personnalisée pour le modèle produit
class ProduitAdmin(admin.ModelAdmin):
    # Afficher les champs souhaités dans la liste des produits
    list_display = ('name', 'categorie', 'price', 'dispo', 'is_sale')
    
    # Ajouter un filtre pour les catégories
    list_filter = ('categorie',)

    # Ordonner les produits par catégorie
    ordering = ('categorie',)

    # Permettre la recherche des produits par nom et catégorie
    search_fields = ('name', 'categorie__name')

# Enregistrer le modèle produit avec la configuration d'administration personnalisée
admin.site.register(produit, ProduitAdmin)
