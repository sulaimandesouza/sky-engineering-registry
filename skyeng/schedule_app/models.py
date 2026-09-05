from django.db import models
from teams_app.models import Engineer, Team

class Meeting(models.Model):
    PLATFORM_CHOICES = [
        ('zoom', 'Zoom'),
        ('meet', 'Google Meet'),
        ('teams', 'Microsoft Teams'),
        ('in_person', 'In Person'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    required_attendees = models.ManyToManyField(
        Engineer, blank=True, related_name='required_meetings'
    )
    optional_attendees = models.ManyToManyField(
        Engineer, blank=True, related_name='optional_meetings'
    )
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default='zoom')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title