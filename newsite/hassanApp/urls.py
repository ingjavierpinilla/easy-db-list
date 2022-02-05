from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<pk>/update", views.HassanAppUpdateView.as_view()),
    path("search", views.search, name="search"),
]
