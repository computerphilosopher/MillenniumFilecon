from django.urls import path
from . import views

app_name = 'upload'

urlpatterns = [
    path('', views.upload_file, name ='upload_file'),
    path('download/', views.download_video),
]
