from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("konrad", views.konrad ,name="konrad1"),
]