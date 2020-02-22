from rest_framework import serializers
from .models import Tyre, TyresGroup


class TyresGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyresGroup
        fields = '__all__'


class TyreSerializer(serializers.ModelSerializer):
    group = TyresGroupSerializer()
    
    class Meta:
        model = Tyre
        fields = '__all__'