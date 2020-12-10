from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def main(request):
    return render(request, "musicapp/main.html")

def index(request):
    # Display recent songs
    if not request.user.is_anonymous:
        recent = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
        recent_id = [each['song_id'] for each in recent][:5]
        recent_songs_unsorted = Song.objects.filter(id__in=recent_id, recent__user=request.user)
        recent_songs = list()
        for id in recent_id:
            recent_songs.append(recent_songs_unsorted.get(id=id))
    else:
        recent = None
        recent_songs = None

    first_time = False
    # Last played song
    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
        if last_played_list:
            last_played_id = last_played_list[0]['song_id']
            last_played_song = Song.objects.get(id=last_played_id)
        else:
            first_time = True
            last_played_song = Song.objects.get(id=1)

    else:
        first_time = True
        last_played_song = Song.objects.get(id=1)

    # Display all songs
    songs = Song.objects.all()

    # Display few songs on home page
    songs_all = list(Song.objects.all().values('id').order_by('?'))
    sliced_ids = [each['id'] for each in songs_all][:5]
    indexpage_songs = Song.objects.filter(id__in=sliced_ids)

    # Display English Songs
    songs_english = list(Song.objects.filter(language='English').values('id'))
    sliced_ids = [each['id'] for each in songs_english][:5]
    indexpage_english_songs = Song.objects.filter(id__in=sliced_ids)

    # Display Chiptune Songs
    songs_chiptune = list(Song.objects.filter(language='Chiptune').values('id'))
    sliced_ids = [each['id'] for each in songs_chiptune][:5]
    indexpage_chiptune_songs = Song.objects.filter(id__in=sliced_ids)

    # Display Neir:Automata Songs
    songs_Nier = list(Song.objects.filter(language='Nier:Automata').values('id'))
    sliced_ids = [each['id'] for each in songs_Nier][:5]
    indexpage_Nier_songs = Song.objects.filter(id__in=sliced_ids)

    # Display DJMAX Songs
    songs_DJMAX = list(Song.objects.filter(language='DJMAX').values('id'))
    sliced_ids = [each['id'] for each in songs_DJMAX][:5]
    indexpage_DJMAX_songs = Song.objects.filter(id__in=sliced_ids)

    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        filtered_songs = songs.filter(Q(name__icontains=search_query)).distinct()
        context = {'all_songs': filtered_songs, 'last_played': last_played_song, 'query_search': True}
        return render(request, 'musicapp/index.html', context)

    context = {
        'all_songs': indexpage_songs,
        'recent_songs': recent_songs,
        'english_songs': indexpage_english_songs,
        'chiptune_songs': indexpage_chiptune_songs,
        'DJMAX_songs': indexpage_DJMAX_songs,
        'Nier_songs': indexpage_Nier_songs,
        'last_played': last_played_song,
        'first_time': first_time,
        'query_search': False,
    }
    return render(request, 'musicapp/index.html', context=context)

def english_songs(request):
    english_songs = Song.objects.filter(language='English')

    # Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=1)

    query = request.GET.get('q')

    if query:
        english_songs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'english_songs': english_songs}
        return render(request, 'musicapp/english_songs.html', context)

    context = {'english_songs': english_songs, 'last_played': last_played_song}
    return render(request, 'musicapp/english_songs.html', context=context)


def chiptune_songs(request):
    chiptune_songs = Song.objects.filter(language='Chiptune')

    # Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=1)

    query = request.GET.get('q')

    if query:
        chiptune_songs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'chiptune_songs': chiptune_songs}
        return render(request, 'musicapp/chiptune_songs.html', context)

    context = {'chiptune_songs': chiptune_songs, 'last_played': last_played_song}
    return render(request, 'musicapp/chiptune_songs.html', context=context)

def Nier_songs(request):
    Nier_songs = Song.objects.filter(language='Nier:Automata')

    # Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=1)

    query = request.GET.get('q')

    if query:
        Nier_songs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'Nier_songs': Nier_songs}
        return render(request, 'musicapp/Nier_songs.html', context)

    context = {'Nier_songs': Nier_songs, 'last_played': last_played_song}
    return render(request, 'musicapp/Nier_songs.html', context=context)

def DJMAX_songs(request):
    DJMAX_songs = Song.objects.filter(language='DJMAX')

    # Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=1)

    query = request.GET.get('q')

    if query:
        Nier_songs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'DJMAX_songs': DJMAX_songs}
        return render(request, 'musicapp/DJMAX_songs.html', context)

    context = {'DJMAX_songs': DJMAX_songs, 'last_played': last_played_song}
    return render(request, 'musicapp/DJMAX_songs.html', context=context)


@login_required(login_url='login')
def play_song(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs, user=request.user).values()):
        data = Recent.objects.filter(song=songs, user=request.user)
        data.delete()
    data = Recent(song=songs, user=request.user)
    data.save()
    return redirect('all_songs')


@login_required(login_url='login')
def play_song_index(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs, user=request.user).values()):
        data = Recent.objects.filter(song=songs, user=request.user)
        data.delete()
    data = Recent(song=songs, user=request.user)
    data.save()
    return redirect('index')


@login_required(login_url='login')
def play_recent_song(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs, user=request.user).values()):
        data = Recent.objects.filter(song=songs, user=request.user)
        data.delete()
    data = Recent(song=songs, user=request.user)
    data.save()
    return redirect('recent')


def all_songs(request):
    songs = Song.objects.all()

    first_time = False
    # Last played song
    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
        if last_played_list:
            last_played_id = last_played_list[0]['song_id']
            last_played_song = Song.objects.get(id=last_played_id)
    else:
        first_time = True
        last_played_song = Song.objects.get(id=1)

    # apply search filters
    qs_singers = Song.objects.values_list('singer').all()
    s_list = [s.split(',') for singer in qs_singers for s in singer]
    all_singers = sorted(list(set([s.strip() for singer in s_list for s in singer])))
    qs_languages = Song.objects.values_list('language').all()
    all_languages = sorted(list(set([l.strip() for lang in qs_languages for l in lang])))

    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        search_singer = request.GET.get('singers') or ''
        search_language = request.GET.get('languages') or ''
        filtered_songs = songs.filter(Q(name__icontains=search_query)).filter(
            Q(language__icontains=search_language)).filter(Q(singer__icontains=search_singer)).distinct()
        context = {
            'songs': filtered_songs,
            'last_played': last_played_song,
            'all_singers': all_singers,
            'all_languages': all_languages,
            'query_search': True,
        }
        return render(request, 'musicapp/all_songs.html', context=context)

    context = {
        'songs': songs,
        'last_played': last_played_song,
        'first_time': first_time,
        'all_singers': all_singers,
        'all_languages': all_languages,
        'query_search': False,
    }
    return render(request, 'musicapp/all_songs.html', context=context)


def recent(request):
    # Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=1)

    # Display recent songs
    recent = list(Recent.objects.filter(user=request.user).values('song_id').order_by('-id'))
    if recent and not request.user.is_anonymous:
        recent_id = [each['song_id'] for each in recent]
        recent_songs_unsorted = Song.objects.filter(id__in=recent_id, recent__user=request.user)
        recent_songs = list()
        for id in recent_id:
            recent_songs.append(recent_songs_unsorted.get(id=id))
    else:
        recent_songs = None

    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        filtered_songs = recent_songs_unsorted.filter(Q(name__icontains=search_query)).distinct()
        context = {'recent_songs': filtered_songs, 'last_played': last_played_song, 'query_search': True}
        return render(request, 'musicapp/recent.html', context)

    context = {'recent_songs': recent_songs, 'last_played': last_played_song, 'query_search': False}
    return render(request, 'musicapp/recent.html', context=context)


@login_required(login_url='login')
def detail(request, song_id):
    songs = Song.objects.filter(id=song_id).first()

    # Add data to recent database
    if list(Recent.objects.filter(song=songs, user=request.user).values()):
        data = Recent.objects.filter(song=songs, user=request.user)
        data.delete()
    data = Recent(song=songs, user=request.user)
    data.save()

    # Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=1)

    playlists = Playlist.objects.filter(user=request.user).values('playlist_name').distinct
    is_favourite = Favourite.objects.filter(user=request.user).filter(song=song_id).values('is_fav')

    if request.method == "POST":
        if 'playlist' in request.POST:
            playlist_name = request.POST["playlist"]
            q = Playlist(user=request.user, song=songs, playlist_name=playlist_name)
            q.save()
            messages.success(request, "재생목록에 음악을 추가하였습니다!")
        elif 'add-fav' in request.POST:
            is_fav = True
            query = Favourite(user=request.user, song=songs, is_fav=is_fav)
            print(f'query: {query}')
            query.save()
            messages.success(request, "좋아하는 음악으로 추가하였습니다!")
            return redirect('detail', song_id=song_id)
        elif 'rm-fav' in request.POST:
            is_fav = True
            query = Favourite.objects.filter(user=request.user, song=songs, is_fav=is_fav)
            print(f'user: {request.user}')
            print(f'song: {songs.id} - {songs}')
            print(f'query: {query}')
            query.delete()
            messages.success(request, "좋아하는 음악에서 삭제되었습니다!")
            return redirect('detail', song_id=song_id)

    context = {'songs': songs, 'playlists': playlists, 'is_favourite': is_favourite, 'last_played': last_played_song}
    return render(request, 'musicapp/detail.html', context=context)


def mymusic(request):
    return render(request, 'musicapp/mymusic.html')


def playlist(request):
    playlists = Playlist.objects.filter(user=request.user).values('playlist_name').distinct
    context = {'playlists': playlists}
    return render(request, 'musicapp/playlist.html', context=context)


def playlist_songs(request, playlist_name):
    songs = Song.objects.filter(playlist__playlist_name=playlist_name, playlist__user=request.user).distinct()

    if request.method == "POST":
        song_id = list(request.POST.keys())[1]
        playlist_song = Playlist.objects.filter(playlist_name=playlist_name, song__id=song_id, user=request.user)
        playlist_song.delete()
        messages.success(request, "재생목록에서 삭제되었습니다!")

    context = {'playlist_name': playlist_name, 'songs': songs}

    return render(request, 'musicapp/playlist_songs.html', context=context)


def favourite(request):
    songs = Song.objects.filter(favourite__user=request.user, favourite__is_fav=True).distinct()
    print(f'songs: {songs}')

    if request.method == "POST":
        song_id = list(request.POST.keys())[1]
        favourite_song = Favourite.objects.filter(user=request.user, song__id=song_id, is_fav=True)
        favourite_song.delete()
        messages.success(request, "좋아하는 음악에서 삭제되었습니다!")
    context = {'songs': songs}
    return render(request, 'musicapp/favourite.html', context=context)