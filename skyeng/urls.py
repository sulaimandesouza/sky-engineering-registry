
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.dashboard, name='dashboard'),
    path('', include('teams_app.urls')),
    path('', include('accounts.urls')),
    path('', include('schedule_app.urls')),
    path('reports/', include('reports_app.urls')),
     path('messages_app/', include('messages_app.urls')),
     ]

#Allows for the reports page to view reports
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

