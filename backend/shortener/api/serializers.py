from rest_framework import serializers

from shortener.models import URL

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ("full_url",)
        
class URLHashedReturnSerializer(serializers.Serializer):
    full_url = serializers.URLField()
    clicks = serializers.IntegerField()
    hashed_url = serializers.URLField()
    created_at = serializers.DateTimeField()