from django.shortcuts import render
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer
from django.contrib.auth.models import User
from  rest_framework.viewsets import ModelViewSet
# Create your views here.
class MenuItemView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = MenuSerializer

# class UserViewSet(ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]