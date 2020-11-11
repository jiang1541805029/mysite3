from rest_framework import serializers
from .models import Jingdian

class JingdianSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jingdian
        fields = ('pk', 'i_d', 'name', 'label', 'address', 'open_time')
