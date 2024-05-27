from django.contrib.auth.forms import UserCreationForm

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Landlord
from .serializer import LandlordSerializer


class SignupView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    model = Landlord
    serializer_class = LandlordSerializer
    form_class = UserCreationForm


class LandlordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
