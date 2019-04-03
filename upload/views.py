from rest_framework import viewsets
#from upload.serializers import UnitSerializer
from django.shortcuts import redirect
from django.shortcuts import render
from django.conf import settings
from upload.models import UploadFileModel
from upload.forms import UploadFileForm
import moviepy.editor as mp

# Create your views here.
    

def download_video(request):
    
    return render(request, 'download_page.html')

def convert(instance):

    root = settings.MEDIA_ROOT 
    
    file_url = root + instance.file.url.split('/')[-1]
    clip = mp.VideoFileClip(file_url)

    video_name = (file_url.split('/')[-1]).split('.')[0]
    clip.write_videofile(video_name)

    instance.converted = video_name


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            convert(instance)
            return redirect('download/')
    else:
        form = UploadFileForm()
    return render(request, 'upload_page.html', {'form': form})