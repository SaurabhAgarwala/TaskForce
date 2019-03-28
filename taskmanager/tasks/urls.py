from django.conf.urls import url
from . import views

app_name = 'tasks'

urlpatterns = [
   url(r'^newtask/$', views.create_task, name="new-task"),
   url(r'^comment/(?P<num>[0-9]+)/$', views.comment, name="comment"),
   url(r'^commentreply/(?P<num>[0-9]+)/$', views.commentreply, name="comment-reply"),
]   