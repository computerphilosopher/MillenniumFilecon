from upload.models import Unit
from rest_framework import serializers

class Unit_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ('first_name', 'gif_file')