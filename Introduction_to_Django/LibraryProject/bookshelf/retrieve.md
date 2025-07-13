# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
print(list(books))

# Output:
# [<Book: 1984 by George Orwell (1949)>]
