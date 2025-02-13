from django.urls import path

from .views import (
    CreateShoppingListView, 
    ListShoppingLists, 
    DetailShoppingListView, 
    DeleteShoppingListView, 
)


urlpatterns = [
    path("erstellen/", CreateShoppingListView.as_view(), name="create_shopping_list"),
    path("meine/", ListShoppingLists.as_view(), name="list_shopping_lists"),
    path("<int:pk>/", DetailShoppingListView.as_view(), name="detail_shopping_list"),
    path("löschen/<int:pk>/", DeleteShoppingListView.as_view(), name="delete_shopping_list"),
]