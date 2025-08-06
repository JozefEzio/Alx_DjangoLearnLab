from django.urls import path, include
from .views import BookList
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r"books_all", BookViewSet, basename="book_all")

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path("books/", BookList.as_view(), name="book-list"),  # Maps to the BookList view
    
    
    # Include the router URLs for BookViewSet (all CRUD operations)
    path("", include(router.urls)),  # This includes all routes registered with
]
