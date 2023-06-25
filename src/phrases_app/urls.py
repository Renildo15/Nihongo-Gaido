from django.urls import path
from phrases_app import  views

app_name = 'phrase'

urlpatterns = [
    path('add_phrase/<int:pk>', views.phrase_create, name='add_phrase'),
    path('update_phrase/<int:pk>', views.phrase_update, name='update_phrase'),
    path('delete_phrase/<int:pk>', views.phrase_delete, name='delete_phrase'),
]
