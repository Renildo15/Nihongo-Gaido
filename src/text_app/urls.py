from django.urls import path
from text_app import views

app_name = "text"

urlpatterns = [
    path('text_options/', views.text_options, name="text_options"),
    path('text_list/', views.text_list, name="text_list"),
    path("add_text/", views.text_create, name="add_text")
]
