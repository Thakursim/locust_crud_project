from rest_framework import serializers
from .models import FillNumbers, CoderHome

class FillSerializer(serializers.ModelSerializer):
  class Meta:
    model = FillNumbers
    fields = ('id', 'number_1', 'number_2', 'number_3', 'text_4')

class CoderHomeSerializer(serializers.ModelSerializer):
  class Meta:
    model = CoderHome
    fields = ('id', 'developer', 'tester', 'infra_dev') 