from django.shortcuts import render

# Create your views here.
def projectData(request):
    return render(request,"Project.html")