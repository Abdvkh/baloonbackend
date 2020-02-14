from rest_framework import serializers
from .models import Tyre

class TyreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tyre
        fields = [
                'url', 'image', 'type', 'code', 'title', 'width',
                'height', 'radius', 'speed_index', 'tread_depth',
                'standard', 'oa_dia', 'max_pressure', 'certificate',
                'distance', 'max_loading'
                ]