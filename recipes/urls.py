from django.urls import path
from . import views


app_name = "recipes"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("recipes/<int:id>/", views.recipe_view, name="recipe"),
    path("recipes/category/<int:category_id>/", views.category_view, name="category"),
]
