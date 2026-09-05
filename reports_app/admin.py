from django.contrib import admin
from django.http import FileResponse
from django.template.loader import render_to_string
import io
from  django.urls import path
from django.http import HttpResponse



from .models import Team, Department, Engineer, Report

#The class below was to test button implementation with the Admin page.
#class TeamAdmin(admin.ModelAdmin):
 #   change_list_template = "admin/reports_app/team/change_list.html"


admin.site.register(Team)
admin.site.register(Department)
admin.site.register(Engineer)
admin.site.register(Report)

