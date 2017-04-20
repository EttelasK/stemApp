from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^studentregister/$', views.studentregister, name='student_register'),
    url(r'^parentregister/$', views.parentregister, name='parent_register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^demerits/$', views.demerit, name='demerits'),
    url(r'^detentions/$', views.detention, name='detentions'),
    url(r'^detentions/(?P<id>[0-9]+)/approve/$', views.detention_approve, name='detentions_approve'),
]