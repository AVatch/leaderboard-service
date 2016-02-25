from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, authentication


from leaderboards.models import Leaderboard

from .serializers import EntrySerializer
from .models import Entry


class ListCreateEntriesAPIView(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100


class RetrieveUpdateDestoryEntriesAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100