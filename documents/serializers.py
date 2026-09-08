from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'file_size', 'uploaded_at', 'status', 'owner']
        read_only_fields = ['id', 'file_size', 'uploaded_at', 'status', 'owner']

    def create(self, validated_data):
        file_obj = validated_data['file']
        validated_data['file_size'] = file_obj.size
        return super().create(validated_data)