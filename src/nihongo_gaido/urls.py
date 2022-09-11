from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nihongo_pages_app.urls', namespace='pages')),
    path('grammar/', include('grammar_app.urls', namespace='grammar')),
    path('phrase/', include('phrases_app.urls', namespace='phrase')),
    path('auth/', include('user_app.urls', namespace='user')),
    
]
