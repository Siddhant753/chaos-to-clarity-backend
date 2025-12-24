from rest_framework import serializers
from .models import RawInput, ProcessedEntry

class RawInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawInput
        fields = '__all__'

class ProcessedEntrySerializer(serializers.ModelSerializer):
    raw_text = serializers.CharField(source = 'raw_input.raw_text')
    class Meta:
        model = ProcessedEntry
        fields = '__all__'