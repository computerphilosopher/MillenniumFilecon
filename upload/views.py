from rest_framework import viewsets
from upload.serializers import UnitSerializer
from upload.models import Unit

# Create your views here.

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    