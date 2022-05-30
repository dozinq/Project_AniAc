from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_safe
from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.serializers import MovieSerializer

from .models import Movie, Genre
import requests
from django.db.models import Q


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.order_by('-popularity')
    page        = int(request.GET.get('p', 1))
    paginator   = Paginator(movies, 8)
    boards      = paginator.get_page(page)
    
    context = {
        'boards': boards,
    }
    return render(request, 'movies/index.html', context)

# @require_safe
# def all(request):
#     movies = Movie.objects.order_by('-popularity')

#     context = {
#         'movies': movies,
#     }
#     return render(request, 'movies/all.html', context)

# @require_safe
# def action(request):
#     movies = Movie.objects.filter(genres=28).order_by('-popularity')

#     context = {
#         'movies': movies,
        
#     }
#     return render(request, 'movies/action.html', context)    

# @require_safe
# def thriller(request):
#     movies = Movie.objects.filter(genres=53).order_by('-popularity')

#     context = {
#         'movies': movies,
        
#     }
#     return render(request, 'movies/thriller.html', context)   

@require_safe
def main(request):
    movies1 = Movie.objects.filter(Q(genres='14') | Q(genres='80')).order_by('-popularity')[:4]
    movies2 = Movie.objects.filter(Q(genres='14') | Q(genres='80')).order_by('-popularity')[4:8]
    movies3 = Movie.objects.filter(Q(genres='14') | Q(genres='80')).order_by('-popularity')[8:12]
    movies4 = Movie.objects.filter(Q(genres='14') | Q(genres='80')).order_by('-popularity')[12:16]
    movies5 = Movie.objects.filter(Q(genres='14') | Q(genres='80')).order_by('-popularity')[16:20]

    movies6 = Movie.objects.filter(release_date__range=["2022-05-01", "2022-05-31"]).order_by('-popularity')[:4]
    movies7 = Movie.objects.filter(release_date__range=["2022-05-01", "2022-05-31"]).order_by('-popularity')[4:8]
    movies8 = Movie.objects.filter(release_date__range=["2022-05-01", "2022-05-31"]).order_by('-popularity')[8:12]
    movies9 = Movie.objects.filter(release_date__range=["2022-05-01", "2022-05-31"]).order_by('-popularity')[12:16]
    movies10 = Movie.objects.filter(release_date__range=["2022-05-01", "2022-05-31"]).order_by('-popularity')[16:20]

    movies11 = Movie.objects.order_by('-vote_average')[:4]
    movies12 = Movie.objects.order_by('-vote_average')[4:8]
    movies13 = Movie.objects.order_by('-vote_average')[8:12]
    movies14 = Movie.objects.order_by('-vote_average')[12:16]
    movies15 = Movie.objects.order_by('-vote_average')[16:20]

    context = {
        'movies1': movies1,
        'movies2': movies2,
        'movies3': movies3,
        'movies4': movies4,
        'movies5': movies5,

        'movies6': movies6,
        'movies7': movies7,
        'movies8': movies8,
        'movies9': movies9,
        'movies10': movies10,

        'movies11': movies11,
        'movies12': movies12,
        'movies13': movies13,
        'movies14': movies14,
        'movies15': movies15,

    }
    return render(request, 'movies/main.html', context)

@api_view(['GET'])
def ajax(request):
    movies = Movie.objects.order_by('-popularity')
    paginator = Paginator(movies, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    serializer = MovieSerializer(page_obj, many=True)

    return Response(serializer.data)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)


# @require_safe
# def recommended(request):
#     if request.user.is_authenticated:
#         movies = Movie.objects.order_by('-vote_average')[:10]
#         context = {
#             'movies' : movies,
#         }
#         return render(request, 'movies/recommended.html', context)
#     return redirect('accounts:login')



def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)

        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')



    

    







