from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^leaderboards', views.ListCreateLeaderboardAPIView),
    url(r'^leaderboards/(?P<pk>[0-9]+)', views.RetrieveUpdateDestoryLeaderboardAPIView)
    url(r'^leaderboards/(?P<pk>[0-9]+)/entries', views.ListLeaderboardEntriesAPIView)
]