from django.shortcuts import render
from rest_framework import generics
from .serializers import TweetSerializers
from .models import Tweet

# Create your views here.


class TweetAV(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializers


class TweetDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializers