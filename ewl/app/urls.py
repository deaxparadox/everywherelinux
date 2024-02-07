from django.urls import path, re_path, include

from . import views

app_name = "app"

urlpatterns = [
    # root path
    path(
        "",
        views.root, 
        name="root"
    )
]
