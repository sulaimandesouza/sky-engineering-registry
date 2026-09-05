from django.contrib import admin
from .models import Team, Department, Engineer

# Register your models here.
admin.site.register(Team)
admin.site.register(Department)
admin.site.register(Engineer)

