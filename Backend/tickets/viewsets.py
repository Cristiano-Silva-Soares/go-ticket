from rest_framework import viewsets
from .models import TicketType, VisitSlot
from .serializers import TicketTypeSerializer, VisitSlotSerializer


class TicketTypeViewSet(viewsets.ModelViewSet):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer


class VisitSlotViewSet(viewsets.ModelViewSet):
    queryset = VisitSlot.objects.all()
    serializer_class = VisitSlotSerializer
