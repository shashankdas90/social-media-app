from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('follow/<int:user_id>/', views.follow_unfollow, name='follow_unfollow'),
    path('search/', views.search_users, name='search_users'),
    path('followers/', views.get_followers, name='get_followers'),
    path('following/', views.get_following, name='get_following'),
]