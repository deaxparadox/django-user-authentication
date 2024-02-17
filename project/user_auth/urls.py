from django.urls import path, re_path, include

from . import views

app_name = "user_auth"

urlpatterns = [
    path("", views.user_login, name="login")
]
