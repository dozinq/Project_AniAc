from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    # path('all/', views.all, name='all'),
    # path('action/', views.action, name='action'),
    # path('thriller/', views.thriller, name='thriller'),
    path('ajax/', views.ajax, name='ajax'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    # path('recommended/', views.recommended, name='recommended'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
]
