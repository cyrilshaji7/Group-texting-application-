from django.contrib import admin
from django.urls import include, path, re_path
from chat.views import index, room

app_name = 'chat'

urlpatterns = [
    path("", index, name='index'),
    path("admin/", admin.site.urls),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name="room"),
    path("chat/", include('chat.urls', namespace='chat')),
]