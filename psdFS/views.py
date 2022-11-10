from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from .models import PSD
# Create your views here.
@csrf_exempt
def handler(request):
    if request.method == 'GET':
        response = {
            'id': 1,
            'name': 'GET'
        }
        return JsonResponse(response)
    elif request.method == 'POST':
        response = {
            'id': 2,
            'name': 'POST'
        }
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['file'].name)
            print(request.POST['num_merge'])
            print(request.POST['merge_condition'])
            print(request.POST['counter'])
            instance = PSD(file=request.FILES['file'])
            instance.save()

        return JsonResponse(response)