from django.urls import path
from . import views
from .views import MyLoginView, MyLogoutView

urlpatterns = [
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', MyLogoutView.as_view(), name='logout'),
    path('signup', views.signup_user, name='signup'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('update_profile/<int:user_id>', views.update_profile, name = 'update-profile'),
    path('update_password/<int:user_id>', views.update_password, name = 'update-password'),
]
