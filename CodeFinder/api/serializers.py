from rest_framework import serializers
from .models import Code, Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'password')

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ('id', 'contribution_title', 'created_at')