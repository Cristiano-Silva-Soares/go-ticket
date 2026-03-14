from rest_framework import serializers
from .models import TicketType, VisitSlot


class TicketTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketType
        fields = "__all__"


class VisitSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisitSlot
        fields = "__all__"