from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, authentication

from .serializers import LeaderboardSerializer
from .serializers import EntrySerializer
from .models import Leaderboard
from .models import Entry


class LeaderboardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100
    
    def perform_create(self, serializer):
        """Automatically set the author to the person making the request"""
        serializer.save(author=self.request.user)


class LeaderboardRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LeaderboardSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100
    
    def get_queryset(self, pk):
        """Only return the leaderboard objects the requester has created"""
        return Leaderboard.objects.filter(author=self.request.user)


class LeaderboardListEntriesAPIView(generics.ListAPIView):
    serializer_class = EntrySerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100
    
    def get_queryset(self, pk):
        leaderboard = get_object_or_404(Leaderboard, pk=pk)
        return Entry.objects.filter(leaderboard=leaderboard)


class EntriesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100


class EntriesRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100