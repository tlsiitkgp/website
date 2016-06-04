from django.conf.urls import url

from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    #url(r'^add_lecture/$', views.add_lecture, name="add_lecture"),
    #url(r'^(?P<subject>[A-Z0-9]+)/$', views.sub_index, name='sub_index'),
    #url(r'^edit/(?P<pk>[0-9]+)/$', views.post_edit, name="post_edit"),
]
