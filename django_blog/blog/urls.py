from django.urls import path
from . import views  # Import your function-based views


urlpatterns = [
    path('', views.home, name='home'),                 # Home page
    path('login/', views.login_user, name='login'),    # Login page
    path('logout/', views.logout_user, name='logout'), # Logout page
    path('register/', views.register_user, name='register'), # Register page
    path('profile/', views.profile, name='profile'),  # Profile page
    path('posts/', views.PostListView.as_view(), name='posts'),  # Posts page
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path("comment/<int:pk>/edit/", views.CommentUpdateView.as_view(), name="comment-edit"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]
