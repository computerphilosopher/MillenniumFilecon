from rest_framework import viewsets
#from upload.serializers import UnitSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render
from upload.models import UploadFileModel
from upload.forms import UploadFileForm

# Create your views here.
    
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    return render(request, 'upload_page.html', {'form': form})