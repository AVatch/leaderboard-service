from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from leaderboards.models import Leaderboard

from .serializers import EntrySerializer
from .models import Entry



class ListEntries(APIView):
    """
    View to list all entries in belonging to a leaderboard.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """
        Return a list of all entries in a leaderboard.
        """
        # usernames = [user.username for user in User.objects.all()]
        return Response([])