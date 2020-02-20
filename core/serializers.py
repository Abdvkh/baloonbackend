from rest_framework import serializers
from .models import Tyre


class TyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tyre
        fields = '__all__'