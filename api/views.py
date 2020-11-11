from django.shortcuts import render
from rest_framework import viewsets
from .models import Jingdian
from .serializers import JingdianSerializers

# Create your views here.
class JingdianViewSet(viewsets.ModelViewSet):
    #指定结果集并设置排序
    queryset = Jingdian.objects.all().order_by('pk')
    #指定序列化的类
    serializer_class = JingdianSerializers