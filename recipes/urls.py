from django.urls import path

from .views import *


urlpatterns = [
    path("generieren/", GenerateRecipeTemplateView.as_view(), name="generate_recipe"),
]
