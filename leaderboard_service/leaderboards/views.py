from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, authentication

from .serializers import LeaderboardSerializer
from .serializers import EntrySerializer
from .models import Leaderboard
from .models import Entry


class ListCreateLeaderboardAPIView(generics.ListCreateAPIView):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveUpdateDestoryLeaderboardAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100


class ListLeaderboardEntriesAPIView(generics.ListAPIView):
    serializer_class = EntrySerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100
    def get_queryset(self, pk):
        leaderboard = get_object_or_404(Leaderboard, pk=self.kwargs['pk'])
        return Entry.objects.filter(leaderboard=leaderboard)


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