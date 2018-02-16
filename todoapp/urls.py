from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signup', views.signup, name="signup"),
    url(r'^login', views.login, name="login"),
    url(r'^reservation', views.reservation, name="reservation"),
    url(r'^start', views.start, name="start"),
    url(r'^washing', views.washing, name="washing"),
    url(r'^complete', views.complete, name="complete"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^(?P<todo_id>[0-9]+)/done/$', views.done, name='done'),
    url(r'^(?P<todo_id>[0-9]+)/delete/$', views.delete, name='delete'),
]
