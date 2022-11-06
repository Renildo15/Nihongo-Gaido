from django.urls import path
from text_app import views

app_name = "text"

urlpatterns = [
    path('text_options/', views.text_options, name="text_options"),
    path('text_list/', views.text_list, name="text_list"),
    path("add_text/", views.text_create, name="add_text"),
    path("text_view/<slug:slug>", views.text_view, name="text_view"),
    path('text_update/<slug:slug>', views.text_update, name="text_update"),
    path('text_delete/<slug:slug>', views.text_delete, name="text_delete")
]
