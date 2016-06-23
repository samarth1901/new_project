from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^key/$', views.index, name='index'),
	url(r'^register/$',views.sign_up,name="sign_up"),
    url(r'^loggedin/$',views.sign_in,name="sign_in"),
    url(r'^update/$',views.update,name="update"),    
    url(r'^log_out/$',views.log_out,name="log_out"),
    url(r'^build_team/$',views.build_team,name="build_team"),
    url(r'^player_profile/$',views.player_profile,name="player_profile"),
    url(r'^search/$',views.search_view,name="search_view"),    
    url(r'^ground/(?P<ground_id>[0-9]+)/$',views.ground_detail, name="ground_detail"),    
    url(r'^team/(?P<team_id>[0-9]+)/$',views.team_detail, name="team_detail"),    
    url(r'^home/(?P<result_id>[0-9]+)/$',views.home_redirect, name="home_redirect"),    
    url(r'^player_game/$',views.player_game,name="player_game"),
    url(r'^owner_profile/$',views.owner_profile,name="owner_profile"),
    url(r'^add_ground/$',views.add_ground,name="add_ground"),
    url(r'^ajax_lookup/(?P<channel>[-\w]+)$', 'ajax_select.views.ajax_lookup', name = 'ajax_lookup'),
]