from rest_framework import viewsets
#from upload.serializers import UnitSerializer
from django.shortcuts import redirect
from django.shortcuts import render
from django.conf import settings
from upload.models import UploadFileModel
from upload.forms import UploadFileForm
import moviepy.editor as mp
import ffmpy

# Create your views here.
    

def download_video(request):
    return render(request, 'download_page.html')

def convert(instance):

    root = settings.MEDIA_ROOT 
    
    file_url = root + '/upload/origin/' + instance.file.url.split('/')[-1]
    file_url = file_url.replace('\\', '/')
    
    video_name = file_url[:-4]
    video_name = video_name.replace("origin", "converted")

    clip = mp.VideoFileClip(file_url)

    clip.write_videofile(video_name +".mp4", fps = 15)

    instance.converted = video_name +".mp4"



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            convert(instance)
            return redirect(instance.converted)
    else:
        form = UploadFileForm()
    return render(request, 'upload_page.html', {'form': form})