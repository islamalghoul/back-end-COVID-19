from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
import requests
from .serializers import CovidSerializer
from .models import Covid
class GlobalStatistics(APIView):
    def get(self,request,format=None):
        url='https://api.covid19api.com/world/total'
        r = requests.get(url).json()
        return Response(r)
        

class LocalStatistics(APIView):
        def get(self,request,format=None):
            country=request.GET['country']
            f=request.GET["from"]
            to=request.GET['to']
            url=f'https://api.covid19api.com/country/{country}/status/confirmed?from={f}&to={to}'
            r = requests.get(url).json()
            return Response(r)

class Summary(APIView):
        serializer_class=CovidSerializer
        def get(self,request,format=None):
            url='https://api.covid19api.com/summary'
            r = requests.get(url).json()
            return Response(r)
        
class CovidListView(ListCreateAPIView):
    queryset=Covid.objects.all()
    serializer_class= CovidSerializer

class CovidDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Covid.objects.all()
    serializer_class= CovidSerializer


