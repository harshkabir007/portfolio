from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def home(request):

    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        return redirect("/#contact")

    context = {
        "skills": Skill.objects.all(),
        "projects": Project.objects.filter(featured=True),
        "experiences": Experience.objects.all(),
        "achievements": Achievement.objects.all(),
    }

    return render(request, "index.html", context)


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    return render(
        request,
        "project_detail.html",
        {
            "project": project,
        },
    )