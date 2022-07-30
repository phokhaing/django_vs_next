"""
+=======================================================+
|| NAME  : PHO KHAING                                  ||
|| EMAIL : khaing.pho1991@gmail.com                    ||
|| DUTY  : FTB BANK (HEAD OFFICE)                      ||
|| ROLE  : Full-Stack Software Developer               ||
+=======================================================+
"""

from django.shortcuts import get_object_or_404
from rest_framework import status, serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Appraisal
from .serializer import AppraisalSerializer


# -------------------------------------
#  API_VIEW
# -------------------------------------
@api_view(['GET'])
def ApiOverview(request):
   return Response([
      '/api/appraisal',
      {
         'Lists': '/all',
         'View': '/view/pk',
         'Add': '/create/',
         'Update': '/update/pk',
         'Delete': '/update/pk'
      }])


# -------------------------------------
#  Method for list all data
# -------------------------------------
@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated]) # Token Authentication
def list_appraisal(request):
   appraisal = Appraisal.objects.all()
   serializer = AppraisalSerializer(appraisal, many=True)
   return Response({
      'success': True,
      'status': status.HTTP_200_OK,
      'message': 'List all appraisal records',
      'data': serializer.data
   })


# -------------------------------------
#  Method for create new data
# -------------------------------------
@api_view(['POST'])
def create_appraisal(request):
   serializer = AppraisalSerializer(data=request.data)
   if Appraisal.objects.filter(**request.data).exists():
      raise serializers.ValidationError("This data already exists!")
   
   if serializer.is_valid():
      serializer.save()
      return Response({
         'success': True,
         'status': status.HTTP_201_CREATED,
         'message': 'Appraisal created successfully.',
         'data': serializer.data
      })
   return Response(status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------
#  Method for update exists data by id
# -------------------------------------
@api_view(['PUT'])
def update_appraisal(request, id):
   appraisal = Appraisal.objects.get(id=id)
   serializer = AppraisalSerializer(instance=appraisal, data=request.data)
   
   if serializer.is_valid():
      serializer.save()
      return Response({
         'success': True,
         'status': status.HTTP_200_OK,
         'message': 'Appraisal updated successfully.',
         'data': serializer.data
      })
   return Response(status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------
#  Method for delete exists data by id
# -------------------------------------
@api_view(['DELETE'])
def delete_appraisal(request, pk):
   serializer = get_object_or_404(Appraisal, pk=pk)
   serializer.delete()
   return Response({
      'success': True,
      'status': status.HTTP_202_ACCEPTED,
      'message': 'Appraisal deleted successfully.',
   })


# -------------------------------------
#  Method for view data by id
# -------------------------------------
@api_view(['GET'])
def view_appraisal(request, id=None):
   appraisal = get_object_or_404(Appraisal, id=id)
   serializer = AppraisalSerializer(appraisal)
   return Response({
      'success': True,
      'status': status.HTTP_200_OK,
      'message': 'List all appraisal records',
      'data': serializer.data
   })
