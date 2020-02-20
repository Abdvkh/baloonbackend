from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TyreSerializer
from .models import Tyre


class TestView(APIView):
    
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, *args, **kwargs):
        qs=Tyre.objects.all()
        serializer = TyreSerializer(qs, many=True)
        # in order to post one instance
        # tyre = qs.first()
        # serializer = TypeSerializer(tyre)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = TyreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)