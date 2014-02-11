from django.http import HttpResponse
from django.shortcuts import render
import logging

from crops.models import Crop, Crop_Detail

def home(request):
    crop_list = Crop.objects.all()
    detail_list = Crop_Detail.objects.all()
    context = {'crop_list': crop_list, 'detail_list' : detail_list }

    return render(request, 'home.html', context)

def detail(request):
    return HttpResponse("Pick weeds or Treatment compare")
