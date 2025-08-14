from django.urls import path
from . import views  # Import your function-based views


urlpatterns = [
    path('', views.home, name='home'),                 # Home page
    path('login/', views.login_user, name='login'),    # Login page
    path('logout/', views.logout_user, name='logout'), # Logout page
    path('register/', views.register_user, name='register'), # Register page
    path('profile/', views.profile, name='profile'),  # Profile page
    path('posts/', views.posts, name='posts'),  # Posts page
]
