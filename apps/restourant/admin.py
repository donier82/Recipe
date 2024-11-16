from django.contrib import admin
from apps.restourant.models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'ingredients', 'instructions', 'preparation_time', 'is_vegetarian']
