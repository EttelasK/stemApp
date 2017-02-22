from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^studentregister/$', views.studentregister, name='student_register'),
    url(r'^parentregister/$', views.parentregister, name='parent_register'),

]