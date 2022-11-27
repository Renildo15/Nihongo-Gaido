from django.urls import path
from vocabulary_app import views

app_name = "vocabulary"

urlpatterns = [
    path("word_list/", views.word_list, name="word_list"),
    path("add_word/", views.word_create, name="add_word"),
    path("edit_word/<slug:slug>", views.word_edit, name="edit_word"),
    path("delete_word/<slug:slug>", views.word_delete, name="delete_word"),
    path("conjugation_list/<slug:slug>", views.conjugation_list, name="conjugation_list"),
    path("add_conjugation/<slug:slug>", views.conjugation_create, name="add_conjugation"),
]
