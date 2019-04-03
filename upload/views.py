from rest_framework import viewsets
#from upload.serializers import UnitSerializer
from django.shortcuts import redirect
from django.shortcuts import render
from upload.models import UploadFileModel
from upload.forms import UploadFileForm

# Create your views here.
    

def download_video(request):
    return render(request, 'download_page.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('download/')
    else:
        form = UploadFileForm()
    return render(request, 'upload_page.html', {'form': form})