from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^leaderboards', views.ListCreateLeaderboardAPIView.as_view()),
    url(r'^leaderboards/(?P<pk>[0-9]+)', views.RetrieveUpdateDestoryLeaderboardAPIView.as_view()),
    url(r'^leaderboards/(?P<pk>[0-9]+)/entries', views.ListLeaderboardEntriesAPIView.as_view())
]