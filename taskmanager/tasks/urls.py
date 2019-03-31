from django.conf.urls import url
from . import views

app_name = 'tasks'

urlpatterns = [
   url(r'^newtask/$', views.create_task, name="new-task"),
   url(r'^newselfassignedtask/$', views.create_selfassigned_task, name="new-selfassignedtask"),
   url(r'^newteamtask/$', views.create_teamtask, name="new-teamtask"),
   url(r'^taskdisplay/(?P<id>[\w-]+)/$', views.task_display, name="task-disp"),
   url(r'^taskedit/(?P<id>[\w-]+)/$', views.task_edit, name="task-edit"),
   url(r'^taskdelete/(?P<id>[\w-]+)/$', views.task_delete, name="task-delete"),
   url(r'^comment/(?P<num>[0-9]+)/$', views.comment, name="comment"),
   url(r'^commentreply/(?P<num>[0-9]+)/$', views.commentreply, name="comment-reply"),
]   