from django.urls import path, include

from .views import *


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("mehr_erfahren/", LearnMoreView.as_view(), name="learn_more"),
    path("über_uns/", AboutUsView.as_view(), name="about_us"),
    path("datenschutz/", DataProtectionView.as_view(), name="data_protection"),
    path("impressum/", ImprintView.as_view(), name="imprint"),
    path("kontakt/", ContactView.as_view(), name="contact"),
    path("tipps/", include("tips.urls")),
    path("rezepte/", include("recipes.urls")),
    path("einkaufslisten/", include("shopping_lists.urls")),
]
