from django.contrib import admin
from django.urls import path, include
from .views import home
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home_page"),
    path('grammar/', include('grammar_app.urls', namespace='grammar')),
]
