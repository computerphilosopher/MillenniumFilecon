from upload.models import Unit
from rest_framework import serializers

class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ('first_name', 'last_name')
