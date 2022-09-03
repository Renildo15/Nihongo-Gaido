from django.urls import path
from grammar_app import views

app_name = 'grammar'

urlpatterns = [
    path('home/', views.index, name='home'),
    path('phrases_list/', views.phrase_list, name='phrases_list'),
    path('update_phrase/<int:pk>', views.phrase_update,name='update_phrase'),
    path('delete_phrase/<int:pk>', views.phrase_delete, name='delete_phrase'),
    path('add/', views.grammar_create, name='add'),
    path('update/<int:pk>', views.grammar_update, name='update'),
    path('delete/<int:pk>', views.grammar_delete, name='delete'),
]
