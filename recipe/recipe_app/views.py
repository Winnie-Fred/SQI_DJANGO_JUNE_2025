from django.shortcuts import render, redirect

from .models import Recipe
from .forms import RecipeForm

# Create your views here.
def recipe_list(request):
    return render(request, "recipe_app/recipe-list.html", {"recipes": Recipe.objects.all()})

def recipe_create(request):
    recipe_form = RecipeForm()
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect('recipe_list')
    context = {
        "recipe_form": recipe_form
    }
    return render(request, "recipe_app/recipe-create.html", context)