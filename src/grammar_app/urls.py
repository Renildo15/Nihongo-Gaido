from django.urls import path
from grammar_app import views

app_name = 'grammar'

urlpatterns = [
    path('grammar_list/', views.grammar_list, name='grammar_list'),
    path('add_grammar/', views.grammar_create, name='add_grammar'),
    path('edit_grammar/<int:pk>', views.grammar_update, name='grammar_edit'),
    path('delete_grammar/<int:pk>', views.grammar_delete, name='grammar_delete'),
]
