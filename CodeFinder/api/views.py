from django.shortcuts import render
from rest_framework import generics
from .serializers import CodeSerializer, AccountSerializer
from .models import Code, Account

# Create your views here.
class CodeView(generics.ListAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

class AccountView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer