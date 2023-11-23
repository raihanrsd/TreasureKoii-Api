from ..models import Hunt, User
from ..serializers import HuntSerializer, UserDataSerializer

from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

class HuntListCreateView(generics.ListCreateAPIView):
    queryset = Hunt.objects.all()
    serializer_class = HuntSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizers=User.objects.filter(id=self.request.user.id))
        
class HuntDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hunt.objects.all()
    serializer_class = HuntSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'