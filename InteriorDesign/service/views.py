from django.shortcuts import render
from .models import Service, TeamMember

# Create your views here.
def index(request):
    services = Service.objects.all()
    teammember = TeamMember.objects.all()
    context = {
        'services': services,
        'teammember': teammember,
    }
    return render(request, 'index.html', context)