from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from .models import RawInput, ProcessedEntry
from .services.classifier import classify_text
from .serializers import ProcessedEntrySerializer
from django.db.models import Count
from django.db.models.functions import TruncDate

@api_view(['GET'])
def api_root(request):
    return Response({
        "input": "/api/input/",
        "entries": "/api/entries/",
        "stats": "/api/stats/",
        "trends": "/api/trends/"
    })

# Accept Raw Input at POST/api/input 
class InputView(APIView):
    def post(self, request):
        text = request.data.get('text')

        if not text:
            return Response({'error' : 'Text is required'}, status= status.HTTP_400_BAD_REQUEST)

        raw = RawInput.objects.create(raw_text = text)
        processed_data = classify_text(text)

        processed = ProcessedEntry.objects.create(raw_input=raw, **processed_data)
            
        return Response(ProcessedEntrySerializer(processed).data, status=status.HTTP_201_CREATED)

# List and Filter at GET/api/entries
class EntryListView(ListAPIView):
    serializer_class = ProcessedEntrySerializer
    
    def get_queryset(self):
        qs = ProcessedEntry.objects.select_related('raw_input')
        category = self.request.query_params.get('category')

        if category:
            qs = qs.filter(category=category)

        return qs.order_by('-created_at')
    
# Analytics at GET/api/stats
class StatsView(APIView):
    def get(self, request):
        data = (ProcessedEntry.objects.values('category').annotate(count=Count('id')))
        return Response(data)

# Time based Insights at GET/api/trends
class TrendView(APIView):
    def get(self, request):
        data = (ProcessedEntry.objects.annotate(date=TruncDate('created_at')).values('date').annotate(count=Count('id')).order_by('date'))
        return Response(data)