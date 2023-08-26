
from django.urls import include, path, re_path
from chat.views import index, room

app_name = 'chat'

urlpatterns = [
    path("", index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name="room"),
]