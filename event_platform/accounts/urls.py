from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('signup', views.signup_user, name='signup'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('update_profile/<int:user_id>', views.update_profile, name = 'update-profile'),
]
