from django.urls import path
from .views import UserRegistration, UserLogin, UserUpdate

urlpatterns = [
    path("signup/", UserRegistration.as_view()),
    path("login/", UserLogin.as_view()),
    path("user-update/", UserUpdate.as_view()),
]
