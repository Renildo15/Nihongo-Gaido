from django.urls import path
from grammar_app import views

app_name = 'grammar'

urlpatterns = [
    path('grammar_list/', views.grammar_list, name='grammar_list'),
    path('add_grammar/', views.grammar_create, name='add_grammar'),
    path('update/<int:pk>', views.grammar_update, name='update'),
    path('delete/<int:pk>', views.grammar_delete, name='delete'),
]
