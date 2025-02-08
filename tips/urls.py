from django.urls import path

from .views import *


urlpatterns = [
    path("", TipListView.as_view(), name="tip_list"),
    path("erstellen/", CreateTipView.as_view(), name="create_tip"),
    path("<int:pk>/", DetailTipView.as_view(), name="detail_tip"),
    path("<int:pk>/bearbeiten/", UpdateTipView.as_view(), name="edit_tip"),
    path("<int:pk>/löschen/", DeleteTipView.as_view(), name="delete_tip"),
]
