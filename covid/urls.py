from django.urls import path
from .views import GlobalStatistics,Summary,LocalStatistics,CovidListView,CovidDetailView
urlpatterns=[

    path('global/',GlobalStatistics.as_view()),
    path('local/',LocalStatistics.as_view()),
    path('summary/',Summary.as_view()),
    path('',CovidListView.as_view()),
    path('<pk>',CovidDetailView.as_view()),


]