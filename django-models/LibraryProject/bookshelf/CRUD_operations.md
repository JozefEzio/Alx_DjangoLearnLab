# CRUD Operations for Book Model

```python
# 1. Book Model Definition (bookshelf/models.py)

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

# 2. Create Operation

from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Output:
# <Book: 1984 by George Orwell (1949)>

# 3. Retrieve Operation

books = Book.objects.all()
print(list(books))

# Output:
# [<Book: 1984 by George Orwell (1949)>]

# 4. Update Operation

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

# Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>

# 5. Delete Operation

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

books = Book.objects.all()
print(list(books))

# Output:
# []
