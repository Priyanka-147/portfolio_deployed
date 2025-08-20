from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('projects', views.portfolio, name='projects'),
    path('about', views.portfolio, name='about'),
    path('contact', views.portfolio, name='contact'),
    path('blogs', views.portfolio, name='blog'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)