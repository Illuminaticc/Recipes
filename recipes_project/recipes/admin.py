from django.contrib import admin
from .models import *
# Register your models here.


class RecipeIngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]


class IngredientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
