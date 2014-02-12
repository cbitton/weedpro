from django.shortcuts import render, get_object_or_404

from treatment.models import Treatment

def index(request):
    latest_treatment_list = Treatment.objects.order_by('name')[:5]
    context = {'latest_treatment_list': latest_treatment_list }
    return render(request, 'treatment/index.html', context)

def detail(request, treatment_id):
    treatment = get_object_or_404(Treatment, pk=treatment_id)
    return render(request, 'treatment/detail.html', {'treatment': treatment})

def timing(request):
    latest_treatment_list = Treatment.objects.order_by('name')[:5]
    context = {'latest_treatment_list': latest_treatment_list }
    return render(request, 'treatment/index.html', context)
