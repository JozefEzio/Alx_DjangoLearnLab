from django.urls import path, include
from .views import BookList
from rest_framework import routers
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r"books_all", BookViewSet, basename="book_all")

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path("books/", BookList.as_view(), name="book-list"),  # Maps to the BookList view
    
    path('auth/token/', obtain_auth_token, name='api_token_auth'), # ✅ Token login endpoint
    # Include the router URLs for BookViewSet (all CRUD operations)
    path("", include(router.urls)),  # This includes all routes registered with
]
