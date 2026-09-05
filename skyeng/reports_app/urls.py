from django.urls import path

from . import views

urlpatterns = [
    path("generate-report/", views.select_team_report, name="select_team_report"),
    path("generate-report/<int:team_id>/", views.generate_team_pdf, name="generate_team_pdf"),
    path('', views.reports_page, name='reports'),
    path('test-pdf/', views.test_pdf, name='test_pdf'),
    path('reports/<int:report_id>/', views.view_report, name="view_report"),
    path("delete-report/<int:report_id>/", views.delete_report, name="delete_report"),
]
