from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^key/$', views.index, name='index'),
	url(r'^register/$',views.sign_up,name="sign_up"),
    url(r'^loggedin/$',views.sign_in,name="sign_in"),
    url(r'^update/$',views.update,name="update"),    
    url(r'^log_out/$',views.log_out,name="log_out"),
    #url(r'^build_team/$',views.build_team,name="build_team"),
    url(r'^player_profile/$',views.player_profile,name="player_profile"),
    url(r'^player_game/$',views.player_game,name="player_game"),
    url(r'^owner_profile/$',views.owner_profile,name="owner_profile"),
    url(r'^add_ground/$',views.add_ground,name="add_ground"),
]