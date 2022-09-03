from dataclasses import fields
from rest_framework import serializers
from .models import Constrain
class ConstrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constrain
        fields = ['year','max_slot_in_day', 'min_slot_in_day', 'max_num_of_days', 'min_num_of_days']
        