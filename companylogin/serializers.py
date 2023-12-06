from .models import *
from rest_framework import serializers

class TestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    test_name = serializers.CharField()
    no_of_questions = serializers.IntegerField()
    total_marks = serializers.IntegerField()
    status = serializers.CharField()
    