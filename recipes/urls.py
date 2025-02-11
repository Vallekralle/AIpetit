from django.urls import path

from .views import *


urlpatterns = [
    path("generieren/", GenerateRecipeFormView.as_view(), name="generate_recipe"),
    path("meine/", RecipeListView.as_view(), name="my_recipe"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("löschen/<int:pk>/", DeleteRecipeView.as_view(), name="delete_recipe"),
    path("save/", SaveRecipeView, name="save_recipe")
]
