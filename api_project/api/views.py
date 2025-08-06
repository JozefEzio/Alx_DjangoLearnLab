from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework.generics import ListAPIView

# Create your views here.


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
