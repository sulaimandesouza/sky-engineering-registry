
from django.http import HttpResponse
try:
    from weasyprint import HTML
    WEASYPRINTWORK = True
except ImportError:
    WEASYPRINTWORK = False
from django.template.loader import render_to_string
from .models import Team, Report
from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
import io
from django.core.files.base import ContentFile
# Create your views here.



#Used to select which team you want to create a report on
def select_team_report(request):
    teams = Team.objects.all()

    if request.method == "POST":
        team_id = request.POST.get("team_id")
        return redirect("generate_team_pdf", team_id=team_id)

    return render(request, "reports_app/select_team.html", {"teams": teams})

#Generates the Team report
def generate_team_pdf(request, team_id):
    if not WEASYPRINTWORK:
        return HttpResponse(
            "PDF generation is unavailble: Weasyprint is not installed on this system."
        )
    team = Team.objects.get(id=team_id)

    report = Report.objects.create(
        name=f"{team.name} Report"
    )

    html_string = render_to_string(
        "reports_app/team_report.html",
        {"team": team}
    )

    pdf = HTML(string=html_string).write_pdf()
    
    filename = f"team_{team_id}_report.pdf"
    report.file.save(filename, ContentFile(pdf))
    report.save()

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="team_{team_id}.pdf"'
    return response

#A test view to see if weasyprint works, not needed to function:
def test_pdf(request):
    if not WEASYPRINTWORK:
        return HttpResponse(
            "PDF generation is unavailble: Weasyprint is not installed on this system."
        )
    html_string = """
    <h1>Report Generating test</h1>
    <p>If this pdf prints, weasyprint works!</p>
    """

    pdf = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="test.pdf"'
    return response


#Shows the currently existing reports
def reports_page(request):
    reports = Report.objects.all()

    query = request.GET.get("search", "")

    if query:
        reports = reports.filter(name__icontains=query)


    return render(request, "reports_app/reports.html", {
        "reports": reports,
        "query":query
    })


#Created to help view stored reports
def view_report(request, report_id):
    return HttpResponse(f"Viewing Report {report_id}")

#Created to delete reports from the report page
def delete_report(request,report_id):
    report = get_object_or_404(Report, id=report_id)

    if report.file:
        report.file.delete(save=False)

    report.delete()

    return redirect("reports")

