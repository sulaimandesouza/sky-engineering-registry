from django.contrib import admin
from .models import Message

# Register Message model to show in Django admin
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = ['subject', 'sender', 'receiver', 'is_read', 'is_draft', 'is_deleted', 'created_at']
    
    # Filter sidebar on the right
    list_filter = ['is_read', 'is_draft', 'is_deleted']
    
    # Search bar at the top
    search_fields = ['subject', 'sender', 'receiver']
    
    # Show newest first
    ordering = ['-created_at']