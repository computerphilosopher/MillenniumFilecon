from rest_framework import viewsets
#from upload.serializers import UnitSerializer
from django.shortcuts import redirect
from django.shortcuts import render
from django.conf import settings
from upload.models import UploadFileModel
from upload.forms import UploadFileForm
from django.http import FileResponse
import moviepy.editor as mp

# Create your views here.
    

def download_video(video_path, request):
    src = {'video_path':video_path}
    return render(request, 'download_page.html', src)

def convert(instance):

    root = settings.MEDIA_ROOT 
    
    file_path = root + '/upload/origin/' + instance.file.url.split('/')[-1]
    file_path = file_path.replace('\\', '/')
    
    video_path = file_path[:-4] + ".mp4"
    video_path = video_path.replace("origin", "converted")

    clip = mp.VideoFileClip(file_path)

    clip.write_videofile(video_path)

    instance.converted = video_path
    instance.converted_url = settings.MEDIA_URL 

    video_name = video_path.split('/')[-1]
    return settings.MEDIA_URL + "upload/converted/" + video_name


def upload_file(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            video_path = convert(instance)
            #return redirect(video_path, download_video)
            return render(request, 'upload_page.html', {'form': form, 'video_path':video_path})
    else:
        form = UploadFileForm()
    return render(request, 'upload_page.html', {'form': form})