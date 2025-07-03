from rest_framework import viewsets
from .models import Donation
from .serializers import DonationSerializer
from rest_framework.permissions import IsAuthenticated

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated]