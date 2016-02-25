from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^entries', views.ListCreateEntriesAPIView.as_view()),
    url(r'^entries/(?P<pk>[0-9]+)', views.RetrieveUpdateDestoryEntriesAPIView.as_view())
]