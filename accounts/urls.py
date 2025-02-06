from django.urls import path

from .views import SignUpView


urlpatterns = [
    path("registrieren/", SignUpView.as_view(), name="signup")
]
