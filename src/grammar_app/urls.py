from django.urls import path
from grammar_app import views

app_name = 'grammar'

urlpatterns = [
    path('grammar_list/', views.grammar_list, name='grammar_list'),
    path('phrases_list/<int:pk>', views.phrase_list, name='phrases_list'),
    path('update_phrase/<int:pk>', views.phrase_update,name='update_phrase'),
    path('delete_phrase/<int:pk>', views.phrase_delete, name='delete_phrase'),
    path('add_grammar/', views.grammar_create, name='add_grammar'),
    path('add_phrase/', views.phrase_create, name='add_phrase'),
    path('update/<int:pk>', views.grammar_update, name='update'),
    path('delete/<int:pk>', views.grammar_delete, name='delete'),
]
