import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "John Doe"
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# List all books in a library
library_name = "City Library"
library = Library.objects.get(name=library_name)
print(f"Books in {library_name}: {[book.title for book in library.books.all()]}")

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library__name=library_name)
print(f"Librarian of {library_name}: {librarian.name}")
