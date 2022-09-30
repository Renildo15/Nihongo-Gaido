from django.urls import path
from phrases_app import  views

app_name = 'phrase'

urlpatterns = [
    path('add_phrase/', views.phrase_create, name='add_phrase'),
    path('phrases_list/<str:pk>', views.phrase_list, name='phrases_list'),
    path('phrase_view/<str:pk>', views.phrase_view, name="phrase_view"),
    path('update_phrase/<str:pk>', views.phrase_update, name='update_phrase'),
    path('delete_phrase/<str:pk>', views.phrase_delete, name='delete_phrase'),
]
