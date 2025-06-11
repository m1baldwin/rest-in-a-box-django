from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from .models import Item
from .serializers import ItemSerializer, UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRetrieveView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def whoami(request):
    return Response({"id": request.user.id, "username": request.user.username})