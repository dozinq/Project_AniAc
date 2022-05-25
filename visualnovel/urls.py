from django.urls import path
from . import views

app_name = 'visualnovel'

urlpatterns = [
    path('', views.index, name='index'),
    path('visualnovel1/', views.visualnovel1, name='visualnovel1'),
    path('visualnovel2/', views.visualnovel2, name='visualnovel2'),
    path('visualnovel3/', views.visualnovel3, name='visualnovel3'),
    path('visualnovel4/', views.visualnovel4, name='visualnovel4'),
    path('result1/<int:slug>/', views.result1, name='result1'),
    path('result2/<int:slug>/', views.result2, name='result2'),
    path('result3/<int:slug>/', views.result3, name='result3'),
    path('result4/<int:slug>/', views.result4, name='result4'),
]