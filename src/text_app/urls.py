from django.urls import path
from text_app import views

app_name = "text"

urlpatterns = [
    path("add_text/", views.text_create, name="add_text")
]
