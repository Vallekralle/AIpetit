from django.urls import path

from .views import *


urlpatterns = [
    path("", TipListView.as_view(), name="tipps")
]
