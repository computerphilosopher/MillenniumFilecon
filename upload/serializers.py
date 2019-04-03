from upload.models import Image
from rest_framework import serializers

class UnitSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url = True)
    class Meta:
        model = Image
        fields = ('gif_name','image')
