from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^edit/(?P<editing_id>\d+)/$', views.edit, name='edit'),
    url(r'^dropshot/$', views.dropshot, name='dropshot'),
    url(r'^addall/$', views.add_all, name='addall'),
    url(r'^view/(?P<member_id>\d+)/$', views.get_message, name='get_message'),
    url(r'^top/$', views.top, name='top'),
    url(r'^top2/$', views.top2, name='top2'),
]
