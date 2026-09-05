from django.shortcuts import render, get_object_or_404
from .models import Team, Department, Engineer
from django.contrib.auth.decorators import login_required


# Create your views here.

from django.shortcuts import render
from .models import Team, Department

# Create your views here.
#def teams(request):
    #return render(request, 'teams_app/teams.html')

def teams(request):
    query = request.GET.get('search')
    
    if query:
        teams = Team.objects.filter(name__icontains=query)
    else:
        teams = Team.objects.all()



    context = {
        'teams' : teams,
        'total_teams' : Team.objects.count(),
        'total_departments' : Department.objects.count(),
        'active_teams' : Team.objects.filter(active=True).count(),
    }

    return render(request, 'teams_app/teams.html', context)

@login_required
def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    engineers = team.engineer_set.all()
    engineers_count = engineers.count()

    skills = []
    if team.skills:
        skills = [skill.strip() for skill in team.skills.split(",")]

    downstream = team.downstream.all()
    upstream = team.upstream.all()

    context = {
        'team': team,
        'engineers': engineers,
        'skills': skills,
        'downstream': downstream,
        'upstream': upstream,
        'engineers_count': engineers_count,
    }

    return render(request, 'teams_app/team_detail.html', context)
