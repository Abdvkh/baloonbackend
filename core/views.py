# from django.shortcuts import render
from django.http import Http404
from .models import Tyre
from rest_framework import generics
from rest_framework import viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response
from .serializers import TyreSerializer
# from rest_framework.exceptions import NotFound

# class TyresView(APIView):
#     def get(self, request, *args, **kwargs):
#         tyres_list = Tyre.objects.all()
#         tyres_api_list_with_info = list()
#
#         for tyre in tyres_list:
#             tyres_api_list_with_info.append({
#                     'code': tyre.code,
#                     'type': tyre.type,
#                     'title': tyre.title,
#                     'size': tyre.get_full_size(),
#                     'speed_index': tyre.speed_index,
#                     'tread_depth': tyre.tread_depth,
#                     'standard': tyre.standard,
#                     'oa_dia': tyre.oa_dia,
#                     'max_pressure': tyre.max_pressure,
#                     'distance': tyre.distance,
#                     'certificate': tyre.certificate,
#                     'max_loading': tyre.max_loading
#                 }
#             )
#
#         return Response(tyres_api_list_with_info)


class TyreViewSet(viewsets.ModelViewSet):
    queryset = Tyre.objects.all()
    serializer_class = TyreSerializer


class SearchViewSet(generics.ListAPIView):
    serializer_class = TyreSerializer

    def get_queryset(self):
        width = self.kwargs['width']
        height = self.kwargs['height']
        radius = self.kwargs['radius']
        return Tyre.objects.filter(width=width, height=height, radius=radius)

        # return Tyre.objects.filter(width=self.request.GET['width'],
        #                            height=self.request.GET['height'],
        #                            radius=self.request.GET['radius']
        #                            )
# def search_by_size(request, width, height, radius):
#     if width > 0 and height > 0 and radius > 0:
#         return Tyre.objects.filter(width=width, height=height, radius=radius)
#     else:
#         raise TimeoutError('Such size is not available now.')