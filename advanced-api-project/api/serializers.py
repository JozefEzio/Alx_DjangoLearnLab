from rest_framework import serializers
from .models import Book
from .models import Author
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    
    """
    BookSerializer:
    - Serializes all fields from the Book model.
    - Includes custom validation to ensure publication_year is not in the future.
    """
    
    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        """
        Check that the publication_year is not greater than the current year.
        """
        current_year = datetime.now().year

        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    
    """
    AuthorSerializer:
    - Serializes the author's name.
    - Includes nested BookSerializer to show all related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
