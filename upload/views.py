from rest_framework import viewsets
from upload.serializers import UnitSerializer
from upload.models import Image

# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = UnitSerializer
    