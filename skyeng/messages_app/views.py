from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from django.db.models import Q

# Inbox view - retrieves all non-draft, non-deleted messages
def inbox(request):
    messages = Message.objects.filter(is_draft=False, is_deleted=False).order_by('-created_at')
    # Handle search query
    query = request.GET.get('q')
    if query:
        messages = messages.filter(Q(subject__icontains=query) | Q(sender__icontains=query))
    return render(request, 'messages_app/inbox.html', {'messages': messages, 'query': query})

# View a single message and mark it as read
def view_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    # Mark as read when opened
    if not message.is_read:
        message.is_read = True
        message.save()
    messages = Message.objects.filter(is_draft=False, is_deleted=False).order_by('-created_at')
    return render(request, 'messages_app/inbox.html', {'messages': messages, 'selected': message})

# Compose view - handles sending new messages and saving drafts
def compose(request):
    if request.method == 'POST':
        receiver = request.POST.get('receiver')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        action = request.POST.get('action')

        # Validate all fields are filled in
        if not receiver or not subject or not body:
            return render(request, 'messages_app/compose.html', {'error': 'All fields are required'})

        if action == 'draft':
            # Save as draft
            Message.objects.create(sender="JD", receiver=receiver, subject=subject, body=body, is_draft=True, is_deleted=False)
            return redirect('drafts')
        else:
            # Send message
            Message.objects.create(sender="JD", receiver=receiver, subject=subject, body=body, is_draft=False, is_deleted=False)
            return redirect('inbox')

    return render(request, 'messages_app/compose.html')

# Sent view - shows all messages sent by current user
def sent(request):
    messages = Message.objects.filter(sender="JD", is_draft=False, is_deleted=False).order_by('-created_at')
    query = request.GET.get('q')
    if query:
        messages = messages.filter(Q(subject__icontains=query) | Q(receiver__icontains=query))
    return render(request, 'messages_app/sent.html', {'messages': messages, 'query': query})

# Drafts view - shows all saved drafts
def drafts(request):
    messages = Message.objects.filter(is_draft=True, is_deleted=False).order_by('-created_at')
    return render(request, 'messages_app/drafts.html', {'messages': messages})

# Trash view - shows deleted messages
def trash(request):
    messages = Message.objects.filter(is_deleted=True).order_by('-created_at')
    return render(request, 'messages_app/trash.html', {'messages': messages})

# Delete view - moves message to trash
def delete_message(request, message_id):
    try:
        message = Message.objects.get(id=message_id)
        message.is_deleted = True
        message.save()
    except Message.DoesNotExist:
        pass
    return redirect('inbox')

# View a single sent message
def view_sent(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    messages = Message.objects.filter(sender="JD", is_draft=False, is_deleted=False).order_by('-created_at')
    query = request.GET.get('q')
    if query:
        messages = messages.filter(Q(subject__icontains=query) | Q(receiver__icontains=query))
    return render(request, 'messages_app/sent.html', {'messages': messages, 'selected': message, 'query': query})

# View a single draft
def view_draft(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    messages = Message.objects.filter(is_draft=True, is_deleted=False).order_by('-created_at')
    return render(request, 'messages_app/drafts.html', {'messages': messages, 'selected': message})

# View a single trash message
def view_trash(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    messages = Message.objects.filter(is_deleted=True).order_by('-created_at')
    return render(request, 'messages_app/trash.html', {'messages': messages, 'selected': message})