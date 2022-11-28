from django.urls import path
from example_app import views

app_name = 'example'

urlpatterns = [
    path('example_list/<slug:slug>', views.example_list, name='example_list'),
    path('add_example/<slug:slug>', views.example_create, name='add_example'),
]
