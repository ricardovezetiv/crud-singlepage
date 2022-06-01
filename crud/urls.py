from django.urls import path

from . import views

app_name = "crud"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("edit/<int:client_id>", views.edit, name="edit"),
    path("delete/<int:client_id>", views.delete, name="delete"),
]
