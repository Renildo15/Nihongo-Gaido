from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nihongo_pages_app.urls', namespace='pages')),
    path('grammar/', include('grammar_app.urls', namespace='grammar')),
    path('phrase/', include('phrases_app.urls', namespace='phrase')),
    path('text/', include('text_app.urls', namespace='text')),
    path('auth/', include('user_app.urls', namespace='user')),
    path('vocabulary/', include('vocabulary_app.urls', namespace='vocabulary')),
    path('example/', include('example_app.urls', namespace='example')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
