from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .serializers import TyreSerializer
from .models import Tyre


class TyresView(APIView):
    
    permission_classes = (AllowAny, )
    
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
    
class TyreViewSet(viewsets.ModelViewSet):
    queryset = Tyre.objects.all()
    serializer_class = TyreSerializer