from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^leaderboards', views.LeaderboardListCreateAPIView.as_view()),
    url(r'^leaderboards/(?P<pk>[0-9]+)', views.LeaderboardRetrieveUpdateDestoryAPIView.as_view()),
    url(r'^leaderboards/(?P<pk>[0-9]+)/entries', views.LeaderboardListEntriesAPIView.as_view()),
    
    url(r'^entries', views.EntriesListCreateAPIView.as_view()),
    url(r'^entries/(?P<pk>[0-9]+)', views.EntriesRetrieveUpdateDestoryAPIView.as_view())
]