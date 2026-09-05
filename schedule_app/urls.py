from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.schedule, name='schedule'),
    path('schedule/meetings/', views.get_meetings, name='get_meetings'),
]