from django.urls import path
from vocabulary_app import views

app_name = "vocabulary"

urlpatterns = [
    path("word_list/", views.word_list, name="word_list"),
]
