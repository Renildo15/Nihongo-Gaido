from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.logar_user, name="logar_user"),
    path('cadastro/', views.cadastrar_user, name="cadastro_user"),
    path('logout/', views.deslogar_user, name="deslogar_user"),
    path('mudar_senha/', views.mudar_senha, name='mudar_senha'),
    path('mudar_senha_sucesso/', views.mudar_senha_sucesso, name='mudar_senha_sucesso'),
]
