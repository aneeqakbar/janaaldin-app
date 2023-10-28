from rest_framework import serializers
from .models import Class, ClassDateTime


class ClassDateTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDateTime
        fields = [
          "parent",
          "datetime",
        ]


class ClassSerializer(serializers.ModelSerializer):
    available_times = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = [
          "name",
          "description",
          "staff_members",
          "available_times",
          "updated_at",
          "created_at",
        ]

    def get_available_times(self, ins):
        available_times = ins.available_times.all()
        serializer = ClassDateTimeSerializer(available_times, many=True)
        return serializer.data
