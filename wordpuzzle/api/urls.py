from django.contrib import admin
from django.urls import path

from .views import WordPuzzleApi

urlpatterns = [
    path("wordpuzzle", WordPuzzleApi.as_view(), name="wordpuzzle"),
]
