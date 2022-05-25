from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_safe
import requests

# Create your views here.

def index(request):
    return render(request, 'visualnovel/index.html')

@require_safe
def visualnovel1(request):
    if request.user.is_authenticated:
        context = {
            'user_name' : request.user.last_name,
        }
        return render(request, 'visualnovel/visualnovel1.html', context)
    return redirect('accounts:login')

@require_safe
def visualnovel2(request):
    if request.user.is_authenticated:
        context = {
            'user_name' : request.user.last_name,
        }
        return render(request, 'visualnovel/visualnovel2.html', context)
    return redirect('accounts:login')

@require_safe
def visualnovel3(request):
    if request.user.is_authenticated:
        context = {
            'user_name' : request.user.last_name,
        }
        return render(request, 'visualnovel/visualnovel3.html', context)
    return redirect('accounts:login')

@require_safe
def visualnovel4(request):
    if request.user.is_authenticated:
        context = {
            'user_name' : request.user.last_name,
        }
        return render(request, 'visualnovel/visualnovel4.html', context)
    return redirect('accounts:login')

def result1(request, slug):
    # 인기순으로 5개만 가져올 것이다. url은 공용 url을 의미한다.
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=d398c62ee408c5afcf987f7c3eb460b4&sort_by=popularity.desc&page=1&language=ko-KR'
    # url_plus는 각 조건에 맞게 추천 결과를 띄울 수 있도록 설정하였다.
    url_plus = ''
    slug = int(slug)

    info_country = slug // 10000
    info_animation = (slug // 1000) % 10
    info_genre = (slug // 100) % 10
    info_latest = (slug % 100) // 10
    info_score = slug % 10

    if info_country == 1:
        url_plus += '&with_original_language=ko'
    elif info_country == 2:
        url_plus += '&with_original_language=au|ca|gb|ie|nz|us'
    elif info_country == 3:
        url_plus += '&with_original_language=ja'
    
    if info_animation == 1:
        url_plus += '&with_genres=16'
    
    if info_genre == 1:
        url_plus += '&with_genres=10749'
    elif info_genre == 2:
        url_plus += '&with_genres=14,12'
    elif info_genre == 3:
        url_plus += '&with_genres=27,53'
    elif info_genre == 4:
        url_plus += '&with_genres=35'
    elif info_genre == 5:
        url_plus += '&with_genres=10751,18'
    
    if info_latest == 1:
        url_plus += '&primary_release_date.gte=2017-05-27'
    
    if info_score == 1:
        url_plus += '&vote_average.gte=8'
    
    # 최종 API_URL은 다음과 같이 표현할 수 있다.
    api_url = url + url_plus
    
    response=requests.get(api_url)
    pop_movies=response.json()

    # 필터링 된 추천 영화의 개수가 5개보다 적다면, 오류를 내지 않고 중복하여 표시될 수 있게 함.
    if len(pop_movies.get('results')) == 4:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[2]
        pop_movies_data4=pop_movies.get('results')[3]
        pop_movies_data5=pop_movies.get('results')[3]
    elif len(pop_movies.get('results')) == 3:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[2]
        pop_movies_data4=pop_movies.get('results')[2]
        pop_movies_data5=pop_movies.get('results')[2]
    elif len(pop_movies.get('results')) == 2:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[1]
        pop_movies_data4=pop_movies.get('results')[1]
        pop_movies_data5=pop_movies.get('results')[1]
    elif len(pop_movies.get('results')) == 1:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[0]
        pop_movies_data3=pop_movies.get('results')[0]
        pop_movies_data4=pop_movies.get('results')[0]
        pop_movies_data5=pop_movies.get('results')[0]
    else:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[2]
        pop_movies_data4=pop_movies.get('results')[3]
        pop_movies_data5=pop_movies.get('results')[4]
        
    context = {
        'pop_movie1' : pop_movies_data1,
        'pop_movie2' : pop_movies_data2,
        'pop_movie3' : pop_movies_data3,
        'pop_movie4' : pop_movies_data4,
        'pop_movie5' : pop_movies_data5,
    }

    return render(request, 'visualnovel/result1.html', context)


def result2(request, slug):
    # 인기순으로 5개만 가져올 것이다. url은 공용 url을 의미한다.
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=567acc586fed43d416e488b297f888a5&sort_by=popularity.desc&page=1&language=ko-KR'
    # url_plus는 각 조건에 맞게 추천 결과를 띄울 수 있도록 설정하였다.
    url_plus = ''
    slug = int(slug)

    info_country = slug // 10000
    info_animation = (slug // 1000) % 10
    info_genre = (slug // 100) % 10
    info_latest = (slug % 100) // 10
    info_score = slug % 10

    if info_country == 1:
        url_plus += '&with_original_language=ko'
    elif info_country == 2:
        url_plus += '&with_original_language=au|ca|gb|ie|nz|us'
    elif info_country == 3:
        url_plus += '&with_original_language=ja'
    
    if info_animation == 1:
        url_plus += '&with_genres=16'
    
    if info_genre == 1:
        url_plus += '&with_genres=10749'
    elif info_genre == 2:
        url_plus += '&with_genres=14,12'
    elif info_genre == 3:
        url_plus += '&with_genres=27,53'
    elif info_genre == 4:
        url_plus += '&with_genres=35'
    elif info_genre == 5:
        url_plus += '&with_genres=10751,18'
    
    if info_latest == 1:
        url_plus += '&primary_release_date.gte=2012-05-27'
    
    if info_score == 1:
        url_plus += '&vote_average.gte=8'
    
    # 최종 API_URL은 다음과 같이 표현할 수 있다.
    api_url = url + url_plus
    
    response=requests.get(api_url)
    pop_movies=response.json()

    # 필터링 된 추천 영화의 개수가 5개보다 적다면, 오류를 내지 않고 중복하여 표시될 수 있게 함.
    if len(pop_movies.get('results')) == 4:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[2]
        pop_movies_data4=pop_movies.get('results')[3]
        pop_movies_data5=pop_movies.get('results')[3]
    elif len(pop_movies.get('results')) == 3:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[2]
        pop_movies_data4=pop_movies.get('results')[2]
        pop_movies_data5=pop_movies.get('results')[2]
    elif len(pop_movies.get('results')) == 2:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[1]
        pop_movies_data4=pop_movies.get('results')[1]
        pop_movies_data5=pop_movies.get('results')[1]
    elif len(pop_movies.get('results')) == 1:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[0]
        pop_movies_data3=pop_movies.get('results')[0]
        pop_movies_data4=pop_movies.get('results')[0]
        pop_movies_data5=pop_movies.get('results')[0]
    else:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[2]
        pop_movies_data4=pop_movies.get('results')[3]
        pop_movies_data5=pop_movies.get('results')[4]
        
    context = {
        'pop_movie1': pop_movies_data1,
        'pop_movie2' : pop_movies_data2,
        'pop_movie3' : pop_movies_data3,
        'pop_movie4' : pop_movies_data4,
        'pop_movie5' : pop_movies_data5,
    }

    return render(request, 'visualnovel/result2.html', context)


def result3(request, slug):
    # 인기순으로 5개만 가져올 것이다. url은 공용 url을 의미한다.
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=d398c62ee408c5afcf987f7c3eb460b4&sort_by=popularity.desc&page=1&language=ko-KR'
    # url_plus는 각 조건에 맞게 추천 결과를 띄울 수 있도록 설정하였다.
    url_plus = ''
    slug = int(slug)

    info_country = slug // 10000
    info_animation = (slug // 1000) % 10
    info_genre = (slug // 100) % 10
    info_latest = (slug % 100) // 10
    info_score = slug % 10

    if info_country == 1:
        url_plus += '&with_original_language=ko'
    elif info_country == 2:
        url_plus += '&with_original_language=au|ca|gb|ie|nz|us'
    elif info_country == 3:
        url_plus += '&with_original_language=ja'
    
    if info_animation == 1:
        url_plus += '&with_genres=16'
    
    if info_genre == 1:
        url_plus += '&with_genres=10749'
    elif info_genre == 2:
        url_plus += '&with_genres=14,12'
    elif info_genre == 3:
        url_plus += '&with_genres=27,53'
    elif info_genre == 4:
        url_plus += '&with_genres=35'
    elif info_genre == 5:
        url_plus += '&with_genres=10751,18'
    
    if info_latest == 1:
        url_plus += '&primary_release_date.gte=2017-05-27'
    
    if info_score == 1:
        url_plus += '&vote_average.gte=8'
    
    # 최종 API_URL은 다음과 같이 표현할 수 있다.
    api_url = url + url_plus
    
    response=requests.get(api_url)
    pop_movies=response.json()

    # 필터링 된 추천 영화의 개수가 5개보다 적다면, 오류를 내지 않고 중복하여 표시될 수 있게 함.
    if len(pop_movies.get('results')) == 4:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[2]
        pop_movies_data4=pop_movies.get('results')[3]
        pop_movies_data5=pop_movies.get('results')[3]
    elif len(pop_movies.get('results')) == 3:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[2]
        pop_movies_data4=pop_movies.get('results')[2]
        pop_movies_data5=pop_movies.get('results')[2]
    elif len(pop_movies.get('results')) == 2:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[1]
        pop_movies_data4=pop_movies.get('results')[1]
        pop_movies_data5=pop_movies.get('results')[1]
    elif len(pop_movies.get('results')) == 1:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[0]
        pop_movies_data3=pop_movies.get('results')[0]
        pop_movies_data4=pop_movies.get('results')[0]
        pop_movies_data5=pop_movies.get('results')[0]
    else:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[2]
        pop_movies_data4=pop_movies.get('results')[3]
        pop_movies_data5=pop_movies.get('results')[4]
        
    context = {
        'pop_movie1' : pop_movies_data1,
        'pop_movie2' : pop_movies_data2,
        'pop_movie3' : pop_movies_data3,
        'pop_movie4' : pop_movies_data4,
        'pop_movie5' : pop_movies_data5,
    }

    return render(request, 'visualnovel/result3.html', context)


# - - - 영화 평가에 대한 함수 ! - - > 새로운 버전.
def result4(request, slug):


    # 인기순으로 5개만 가져올 것이다. url은 공용 url을 의미한다.
    url = 'https://api.themoviedb.org/3/movie/'
    # url_plus는 각 조건에 맞게 추천 결과를 띄울 수 있도록 설정하였다.
    url_plus = ''
    slug = int(slug)

    # 명량
    info_1 = slug // 100000000
    # 극한직업
    info_2 = (slug // 10000000) % 10
    # 신과 함께
    info_3 = (slug // 1000000) % 10
    # 국제시장
    info_4 = (slug // 100000) % 10
    # 어벤져스
    info_5 = (slug // 10000) % 10
    # 겨울왕국
    info_6 = (slug // 1000) % 10
    # 베테랑
    info_7 = (slug // 100) % 10
    # 도둑들
    info_8 = (slug // 10) % 10
    # 7번방의 선물
    info_9 = slug % 10


    if info_1 == 1:
        url_plus += '282631|'
    if info_2 == 1:
        url_plus += '567646|'
    if info_3 == 1:
        url_plus += '397567|'
    if info_4 == 1:
        url_plus += '313108|'
    if info_5 == 1:
        url_plus += '299534|'
    if info_6 == 1:
        url_plus += '109445|'
    if info_7 == 1:
        url_plus += '346646|'
    if info_8 == 1:
        url_plus += '124157|'
    if info_9 == 1:
        url_plus += '158445|'

    
    # 최종 API_URL은 다음과 같이 표현할 수 있다.
    api_url = url + url_plus + '/similar?api_key=d398c62ee408c5afcf987f7c3eb460b4&language=ko-KR&page=1'

    # 어떤 대답에도 '그렇다'라고 대답을 하지 않는다면, 인기영화를 추천할 수 있도록 하였다.
    if url_plus == '':
        api_url = 'https://api.themoviedb.org/3/discover/movie?api_key=d398c62ee408c5afcf987f7c3eb460b4&sort_by=popularity.desc&page=1&language=ko-KR'
    
    response=requests.get(api_url)
    pop_movies=response.json()

    # 필터링 된 추천 영화의 개수가 5개보다 적다면, 오류를 내지 않고 중복하여 표시될 수 있게 함.
    if len(pop_movies.get('results')) == 4:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[2]
        pop_movies_data4=pop_movies.get('results')[3]
        pop_movies_data5=pop_movies.get('results')[3]
    elif len(pop_movies.get('results')) == 3:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[2]
        pop_movies_data4=pop_movies.get('results')[2]
        pop_movies_data5=pop_movies.get('results')[2]
    elif len(pop_movies.get('results')) == 2:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[1]
        pop_movies_data4=pop_movies.get('results')[1]
        pop_movies_data5=pop_movies.get('results')[1]
    elif len(pop_movies.get('results')) == 1:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[0]
        pop_movies_data3=pop_movies.get('results')[0]
        pop_movies_data4=pop_movies.get('results')[0]
        pop_movies_data5=pop_movies.get('results')[0]
    else:
        pop_movies_data1=pop_movies.get('results')[0]
        pop_movies_data2=pop_movies.get('results')[1]
        pop_movies_data3=pop_movies.get('results')[2]
        pop_movies_data4=pop_movies.get('results')[3]
        pop_movies_data5=pop_movies.get('results')[4]
        
    context = {
        'pop_movie1' : pop_movies_data1,
        'pop_movie2' : pop_movies_data2,
        'pop_movie3' : pop_movies_data3,
        'pop_movie4' : pop_movies_data4,
        'pop_movie5' : pop_movies_data5,
    }

    return render(request, 'visualnovel/result4.html', context)



# 네이버 API를 통한 영화 검색 코드 -> 사용 X : query값이 필수라서 키워드를 입력해서 검색하는 방식이라 사용하지 않음.
# def result(request):
#     headers = {
#         'Host': 'openapi.naver.com',
#         'User-Agent': 'curl/7.49.1',
#         'Accept': '*/*',
#         'X-Naver-Client-Id': '',
#         'X-Naver-Client-Secret': '',
#     }

#     url= 'https://openapi.naver.com/v1/search/movie.json'

#     params = {
#         'query': '',
#         'display': '3',
#         'genre': 5,
#         'country': 'KR',
#         'yearfrom': '2015',
#         'yearto': '2022',
#     }
    
#     response=requests.get(url, headers=headers, params=params)

#     top_movies=response.json()
#     # top_movies_data1=top_movies.get('results')[0:2]
#     # top_movies_data1=top_movies.get('response')
#     # top_movies_data2=top_movies.get('results')[1]
#     # top_movies_data3=top_movies.get('results')[2]

    
#     context = {
#         'top_movies': top_movies
#         # 'top_movies2' : top_movies_data2,
#         # 'top_movies3' : top_movies_data3,
#     }

#     return render(request, 'visualnovel/result.html', context)