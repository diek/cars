from rest_framework import serializers

from . import models


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Car
        fields = [
            "year",
            "model",
            "base_color",
            "size",
        ]


class MakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Make
        fields = [
            "make",
        ]
