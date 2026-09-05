from django import forms
from .models import Meeting
from teams_app.models import Engineer

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = [
            'title', 'date', 'start_time', 'end_time',
            'platform', 'required_attendees', 'optional_attendees',
            'description'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Meeting title'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'start_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'end_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'platform': forms.Select(attrs={
                'class': 'form-control'
            }),
            'required_attendees': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'size': '4'
            }),
            'optional_attendees': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'size': '4'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Description (optional)'
            }),
        }