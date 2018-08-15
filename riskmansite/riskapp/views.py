from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RiskTypes
from .serializers import RiskEntriesSerializer,RiskTypesSerializer
from rest_framework.parsers import JSONParser

# Create your views here.


def index(req):
    return HttpResponse("Holaaaaa")



class RiskTypeList(APIView):
    def get(self,req,format=None):
        risktypes = RiskTypes.objects.all()
        serializer = RiskTypesSerializer(risktypes,many=True)
        return Response(serializer.data)

class RiskTypeItems(APIView):
    def get(self,req,format=None):
        code_param = self.kwargs['code']
        risktype = RiskTypes.objects.filter(code=code_param)

class RiskTypeItem(APIView):
    def get(self,req,format=None):
        risktype = RiskTypes.objects.filter()