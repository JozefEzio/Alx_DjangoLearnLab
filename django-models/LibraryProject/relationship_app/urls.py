from django.urls import path
from .views import list_books, LibraryDetailView, librarian_view, admin_view, member_view
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),
    path("admin-role/", admin_view, name="admin_view"),
    path("librarian-role/", librarian_view, name="librarian_view"),
    path("member-role/", member_view, name="member_view"),
]
