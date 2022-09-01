from django.urls import path
from grammar_app import views

app_name = 'grammar'

urlpatterns = [
    path('home/', views.index, name='home'),
    path('add/', views.grammar_create, name='add'),
    path('update/<int:pk>', views.grammar_update, name='update'),
    path('delete/<int:pk>', views.grammar_delete, name='delete'),
]
