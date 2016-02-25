from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics


from entries.models import Entry
from entries.serializers import EntrySerializer

from .serializers import LeaderboardSerializer
from .models import Leaderboard


class ListCreateLeaderboardAPIView(generics.ListCreateAPIView):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100


class RetrieveUpdateDestoryLeaderboardAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100


class ListLeaderboardEntriesAPIView(generics.ListAPIView):
    serializer_class = EntrySerializer
    authentication_classes = (authentication.TokenAuthentication,)
    paginate_by = 100
    def get_queryset(self):
        leaderboard = get_object_or_404(Leaderboard, pk=self.kwargs['pk'])
        return Entry.objects.filter(leaderboard=leaderboard)