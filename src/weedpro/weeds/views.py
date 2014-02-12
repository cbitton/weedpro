from django.shortcuts import render, get_object_or_404

from weeds.models import Weed

def index(request):
    latest_weed_list = Weed.objects.order_by('name')
    context = {'latest_weed_list': latest_weed_list }
    return render(request, 'weeds/index.html', context)

def detail(request, weed_id):
    weed = get_object_or_404(Weed, pk=weed_id)
    return render(request, 'weeds/detail.html', {'weed': weed})

