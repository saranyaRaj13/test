
from rest_framework import serializers

from Document.models import DocumentModel, CargoShip, Cargo


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=DocumentModel
        fields=("__all__")
class CargoShipSerializer(serializers.ModelSerializer):
    class Meta:
        model=CargoShip
        fields=("__all__")
class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cargo
        fields=("__all__")

