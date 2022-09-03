from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from . import views

urlpatterns = [
    path("accounts/", views.RegisterView.as_view()),
    path("login/", ObtainAuthToken.as_view()),
]
