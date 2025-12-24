from django.urls import path
from .views import InputView, EntryListView, StatsView, TrendView, api_root

urlpatterns = [
    path('', api_root),
    path('input/', InputView.as_view()),
    path('entries/', EntryListView.as_view()),
    path('stats/', StatsView.as_view()),
    path('trends/', TrendView.as_view()),
]
