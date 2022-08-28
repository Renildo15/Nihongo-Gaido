from django.urls import path
from grammar_app import views

app_name = 'grammar'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/', views.grammar_create, name='add'),
]
