from django.urls import path
from . import views

# Add URLConf
urlpatterns = [
    path('', views.v_index, name='v_index'),
    path('<int:video_id>/', views.v_detail, name='v_detail'),
    path('all_video', views.all_video, name='all_video'),
    path('game_video', views.game_video, name='game_video'),
    path('anime_video', views.anime_video, name='anime_video'),
    path('vlog_video', views.vlog_video, name='vlog_video'),
]
