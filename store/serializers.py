from rest_framework import serializers

class UpdateCartSerializer(serializers.Serializer):
    action = serializers.CharField()
    productId = serializers.IntegerField()

class ShippingInformationSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True)
    email = serializers.CharField(required=False, allow_blank=True)
    location = serializers.CharField()
    estate = serializers.CharField()
    house_no = serializers.CharField()