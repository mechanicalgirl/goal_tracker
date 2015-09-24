from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^closedateset/(?P<id>\w+)/*$',        views.close_dateset,    name='close_dateset'),
    url(r'^addactivity/(?P<id>\w+)/*$',         views.add_activity,     name='add_activity'),
    url(r'^goalset/',                           views.goal_set,         name='create_goal_set'),
    url(r'^goaladd/',                           views.goal_add,         name='add_new_goal'),
    url(r'^summary/(?P<id>\w+)/*$',             views.show_summary,     name='goals_summary'),
    url(r'^summary/*$',                         views.show_summary,     name='goals_summary'),
    url(r'^getstarted/',                        views.show_home,        name='get_started'),
    url(r'^$',                                  views.show_home,        name='goals_home'),
]
