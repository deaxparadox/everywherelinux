# from django.shortcuts import (
#     render,
#     get_object_or_404,
#     redirect
# )
# from typing import Any
# from django.http import HttpRequest, HttpResponse
# from django.urls import path
# from django.views.generic import ListView

# from .models import URL


# def index(request):
#     return render(
#         request,
#         "shortener/index.html"
#     )
    
# class IndexView(ListView):
#     model = URL
#     templates = ""