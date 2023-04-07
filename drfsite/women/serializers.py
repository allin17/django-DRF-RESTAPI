import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from women.models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = "__all__"
