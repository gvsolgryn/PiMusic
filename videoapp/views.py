from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def v_index(request):
    # 비디오 관련 DB 오브젝트를 videos 에 모두 저장
    videos = Video.objects.all()

    # 모든 영상중 5개의 영상을 index 화면에 띄우기
    videos_all = list(Video.objects.all().values('id').order_by('?'))
    sliced_ids = [each['id'] for each in videos_all][:5]
    indexpage_videos = Video.objects.filter(id__in=sliced_ids)

    # 게임(플레이) 영상 index 화면에 띄우가
    videos_games = list(Video.objects.filter(tag='Games').values('id'))
    sliced_ids = [each['id'] for each in videos_games][:5]
    indexpage_game_videos = Video.objects.filter(id__in=sliced_ids)

    # Vlog(도네용) 영상 index 화면에 띄우가
    videos_vlog = list(Video.objects.filter(tag='Vlog').values('id'))
    sliced_ids = [each['id'] for each in videos_vlog][:5]
    indexpage_vlog_videos = Video.objects.filter(id__in=sliced_ids)

    # Anime(애니) 영상 index 화면에 띄우가
    videos_anime = list(Video.objects.filter(tag='Anime').values('id'))
    sliced_ids = [each['id'] for each in videos_anime][:5]
    indexpage_anime_videos = Video.objects.filter(id__in=sliced_ids)

    context = {
        'videos': videos,
        'all_video': indexpage_videos,
        'game_video': indexpage_game_videos,
        'vlog_video': indexpage_vlog_videos,
        'anime_video': indexpage_anime_videos,
    }
    return render(request, "videoapp/v_index.html", context)

def v_detail(request, video_id):
    videos = Video.objects.filter(id=video_id).first()

    context = {
        'video': videos,
    }
    return render(request, "videoapp/v_detail.html", context)

def all_video(request):
    videos = Video.objects.all()

    videos_all = list(Video.objects.all().values('id'))
    sliced_ids = [each['id'] for each in videos_all]
    all_page_videos = Video.objects.filter(id__in=sliced_ids)

    context = {
        'video': videos,
        'all_video': all_page_videos
    }
    return render(request, "videoapp/all_video.html", context)

def game_video(request):
    videos = Video.objects.all()

    videos_game = list(Video.objects.filter(tag='Games').values('id'))
    sliced_ids = [each['id'] for each in videos_game]
    game_page_videos = Video.objects.filter(id__in=sliced_ids)

    context = {
        'video': videos,
        'game_video': game_page_videos
    }
    return render(request, "videoapp/game_video.html", context)

def anime_video(request):
    videos = Video.objects.all()

    videos_anime = list(Video.objects.filter(tag='Anime').values('id'))
    sliced_ids = [each['id'] for each in videos_anime]
    anime_page_videos = Video.objects.filter(id__in=sliced_ids)

    context = {
        'video': videos,
        'anime_video': anime_page_videos
    }
    return render(request, "videoapp/anime_video.html", context)

def vlog_video(request):
    videos = Video.objects.all()

    videos_vlog = list(Video.objects.filter(tag='Vlog').values('id'))
    sliced_ids = [each['id'] for each in videos_vlog]
    vlog_page_videos = Video.objects.filter(id__in=sliced_ids)

    context = {
        'video': videos,
        'vlog_video': vlog_page_videos
    }
    return render(request, "videoapp/vlog_video.html", context)

