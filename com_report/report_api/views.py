from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from django.contrib.auth.models import User, Group
from .models import *
from .serializers import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportView(viewsets.ModelViewSet):
    queryset = Report.objects.all()

    @extend_schema(responses= ReportSerializer)
    def list (self, request):
        serializer = ReportSerializer(self.queryset, many=True)
        return Response(serializer.data)