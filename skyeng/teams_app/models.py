from django.db import models

# Create your models here.

# REFERENCE: https://docs.djangoproject.com/en/6.0/topics/db/models/

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100) 
    department = models.ForeignKey(Department, on_delete=models.CASCADE) # if department is deleted its teams are deleted
    leader = models.OneToOneField( # each team must have at most one leader
        'Engineer',
        on_delete=models.SET_NULL, # if team leader is deleted, leader becomes NULL
        null=True,
        blank=True,
        related_name='leads_team' #allows engineer to view team that it leads
    )
    active = models.BooleanField(default=True)
    skills = models.TextField(blank=True)
    email = models.EmailField(blank=True)

    downstream = models.ManyToManyField(
        'self', 
        symmetrical=False,
        blank=True,
        related_name='upstream'
    )

    def __str__(self):
        return self.name


class Engineer(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name