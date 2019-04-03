from upload.models import Unit
from rest_framework import serializers

class UnitSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url = True)
    class Meta:
        model = Unit
        fields = ('first_name', 'last_name', 'image')
