from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('inbox/', views.inbox, name='inbox'),
    path('compose/', views.compose, name='compose'),
    path('sent/', views.sent, name='sent'),
    path('drafts/', views.drafts, name='drafts'),
    path('trash/', views.trash, name='trash'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('view/<int:message_id>/', views.view_message, name='view_message'),
    path('view/sent/<int:message_id>/', views.view_sent, name='view_sent'),
    path('view/draft/<int:message_id>/', views.view_draft, name='view_draft'),
    path('view/trash/<int:message_id>/', views.view_trash, name='view_trash'),
]