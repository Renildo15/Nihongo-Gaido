from django.urls import path
from nihongo_pages_app import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
]
