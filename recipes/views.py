from django.shortcuts import render, get_object_or_404, get_list_or_404

# from utils.recipes.factory import make_recipe
from .models import Recipe


def home_view(request):
    recipe = Recipe.objects.filter(is_published=True).order_by("-id")
    return render(
        request,
        "recipes/pages/home_view.html",
        status=200,
        context={"recipes": recipe},
    )


def category_view(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True
    ).order_by("-id")

    recipes = get_list_or_404(recipes)
    return render(
        request,
        "recipes/pages/category_view.html",
        status=200,
        context={
            "recipes": recipes,
            "title": f"{recipes[0].category.name} - Category | ",
            # "title": f"{recipes.first().category.name} - Category | ",
        },
    )


def recipe_view(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    return render(
        request,
        "recipes/pages/recipe_view.html",
        status=200,
        context={
            "recipe": recipe,
            "is_detail_page": True,
        },
    )
