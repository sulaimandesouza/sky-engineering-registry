from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Meeting
from .forms import MeetingForm
from teams_app.models import Team
from django.utils import timezone

def schedule(request):
    form = MeetingForm()

    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule')

    upcoming = Meeting.objects.filter(
        date__gte=timezone.now().date()
    ).order_by('date', 'start_time')[:5]

    teams = Team.objects.all()

    context = {
        'form': form,
        'upcoming': upcoming,
        'teams': teams,
    }
    return render(request, 'schedule_app/schedule.html', context)


def get_meetings(request):
    meetings = Meeting.objects.prefetch_related('required_attendees', 'optional_attendees').all()
    colors = [
        '#2563eb', '#16a34a', '#dc2626', '#9333ea',
        '#ea580c', '#0891b2', '#ca8a04', '#db2777',
    ]
    team_colors = {}
    color_index = 0

    events = []
    for meeting in meetings:
        team_id = meeting.team_id
        if team_id not in team_colors:
            team_colors[team_id] = colors[color_index % len(colors)]
            color_index += 1

        required = [e.name for e in meeting.required_attendees.all()]
        optional = [e.name for e in meeting.optional_attendees.all()]

        events.append({
            'title': meeting.title,
            'start': f"{meeting.date}T{meeting.start_time}",
            'end': f"{meeting.date}T{meeting.end_time}",
            'color': team_colors[team_id],
            'extendedProps': {
                'description': meeting.description,
                'platform': meeting.get_platform_display(),
                'team': str(meeting.team) if meeting.team else 'No team',
                'required': required,
                'optional': optional,
                'date': str(meeting.date),
                'start_time': str(meeting.start_time)[:5],
                'end_time': str(meeting.end_time)[:5],
            }
        })
    return JsonResponse(events, safe=False)