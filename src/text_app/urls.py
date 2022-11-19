from django.urls import path
from text_app import views

app_name = "text"

urlpatterns = [
    path('text_options/', views.text_options, name="text_options"),
    path('text_list/', views.text_list, name="text_list"),
    path('add_text/', views.text_create, name="add_text"),
    path('text_view/<slug:slug>', views.text_view, name="text_view"),
    path('text_update/<slug:slug>', views.text_update, name="text_update"),
    path('text_delete/<slug:slug>', views.text_delete, name="text_delete"),
    path('text_traducao_form/<slug:slug>', views.text_traducao_create, name="add_text_traducao"),
    path('text_traducao_view/<slug:slug>', views.text_traducao_view, name="text_traducao_view"),
    path('text_traducao_update/<slug:slug>', views.text_traducao_update, name="text_traducao_update"),
    path('text_traducao_delete/<slug:slug>', views.text_traducao_delete, name="text_traducao_delete"),
    path('text_escrito_list/', views.text_list_w, name="text_escrito_list"),
    path('text_escrito_form/', views.text_create_w, name="text_escrito_form"),
    path('text_escrito_view/<slug:slug>', views.text_view_w, name="text_escrito_view"),
    path('text_escrito_w/<slug:slug>', views.text_update_w, name="text_escrito_w")
]
