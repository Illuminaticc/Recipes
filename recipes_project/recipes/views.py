from django.shortcuts import render
from django.db.models import Q
from recipes.models import Recipe
# Create your views here.


def recipes_page(request):
    search_query = request.GET.get('search', '')
    if search_query:
        recipes = Recipe.objects.filter(Q(name__icontains=search_query) | Q(ingredients__name__icontains=search_query))
    else:
        recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes.distinct()})
