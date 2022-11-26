from django.urls import path
from vocabulary_app import views

app_name = "vocabulary"

urlpatterns = [
    path("word_list/", views.word_list, name="word_list"),
    path("conjugation_list/<slug:slug>", views.conjugation_list, name="conjugation_list"),
]
