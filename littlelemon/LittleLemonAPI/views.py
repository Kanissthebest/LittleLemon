from django.shortcuts import render
from LittleLemonAPI.serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})