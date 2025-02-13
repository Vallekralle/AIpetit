from django.urls import path

from .views import (
    CreateShoppingListView, 
    ListShoppingLists, 
    DetailShoppingListView, 
    DeleteShoppingListView,
    DeleteBulletPointView,
    AddBulletPointView,
    CheckBulletPointView,
)


urlpatterns = [
    path("erstellen/", CreateShoppingListView.as_view(), name="create_shopping_list"),
    path("meine/", ListShoppingLists.as_view(), name="list_shopping_lists"),
    path("<int:pk>/", DetailShoppingListView.as_view(), name="detail_shopping_list"),
    path("löschen/<int:pk>/", DeleteShoppingListView.as_view(), name="delete_shopping_list"),
    path("bullet_point/hinzufügen/<int:pk>/", AddBulletPointView, name="add_bulletpoint"),
    path("bullet_point/löschen/<int:pk>/", DeleteBulletPointView, name="delete_bulletpoint"),
    path("bullet_point/markieren/<int:pk>/", CheckBulletPointView, name="check_bulletpoint"),
]