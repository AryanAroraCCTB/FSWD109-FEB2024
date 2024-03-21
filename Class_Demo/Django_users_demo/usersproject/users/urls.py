from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_list),
    path("<int:id>", views.user_detail),
    path("create", views.user_create),
    path("<int:id>/update", views.user_update),
    path("<int:id>/delete", views.user_delete),
]
