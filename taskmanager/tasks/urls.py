from django.conf.urls import url
from . import views

app_name = 'tasks'

urlpatterns = [
   url(r'^newtask/$', views.create_task, name="new-task")
]   