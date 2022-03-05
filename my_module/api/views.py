from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework import serializers, viewsets, generics, status


class TestThisAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'res': 'OK!'}, status=status.HTTP_200_OK)
