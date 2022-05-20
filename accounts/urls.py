from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/reviews/', views.reviews, name='reviews'),
    path('<username>/comments/', views.comments, name='comments'),
]
