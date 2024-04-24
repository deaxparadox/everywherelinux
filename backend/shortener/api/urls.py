from django.urls import path

from shortener.api import views

app_name = "shortener_api"

urlpatterns = [
    path("", views.index, name="index"),
]
