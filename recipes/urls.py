from django.urls import path

from .views import *


urlpatterns = [
    path("generieren/", GenerateRecipeFormView.as_view(), name="generate_recipe"),
    path("meine/", RecipeListView.as_view(), name="my_recipe"),
    path("save/", SaveRecipeView, name="save_recipe")
]
