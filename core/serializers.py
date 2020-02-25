from rest_framework import serializers
from .models import Tyre, TyresGroup, Images

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
        
class TyresGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyresGroup
        fields = '__all__'


class TyreSerializer(serializers.ModelSerializer):
    group = TyresGroupSerializer()
    images = ImagesSerializer(many=True)
    class Meta:
        model = Tyre
        fields = '__all__'