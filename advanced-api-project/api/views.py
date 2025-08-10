from django.shortcuts import render
from .models import Author, Book
from rest_framework import generics
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters

# Create your views here.

class BookListView(generics.ListAPIView):
    """
    BookListView:
    - GET /books/
    - Returns a list of all books in the database.
    - Accessible to everyone (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    # filter_backends = [filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] # integrate all filters
    
    # Allow filtering by these fields (exact matches)
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Enable search on these fields (partial, case-insensitive)
    search_fields = ['title', 'author']
    
    
    
class BookDetailView(generics.RetrieveAPIView):
    """
    BookDetailView:
    - GET /books/<id>/
    - Returns a single book by its primary key (id).
    - Accessible to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class BookCreateView(generics.CreateAPIView):
    """
    BookCreateView:
    - POST /books/create/
    - Allows authenticated users to add a new book.
    - Validates data via BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        """
        Custom save logic:
        - Assigns the current logged-in user as the author automatically.
        """
        serializer.save(author=self.request.user)
    
class BookUpdateView(generics.UpdateAPIView):
    """
    BookDeleteView:
    - DELETE /books/<id>/delete/
    - Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def perform_update(self, serializer):
        """
        Custom save logic:
        - Assigns the current logged-in user as the author automatically.
        """
        serializer.save(author=self.request.user)
    
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]