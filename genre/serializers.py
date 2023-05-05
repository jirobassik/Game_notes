from rest_framework import serializers

class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, write_only=True)
    name = serializers.CharField(max_length=70, allow_null=False, allow_blank=False)
    description = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
