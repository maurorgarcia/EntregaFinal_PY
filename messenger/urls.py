from django.urls import path

from . import views

app_name = "messenger"

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("sent/", views.sent, name="sent"),
    path("compose/", views.compose, name="compose"),
]

