# Create Operation

```python
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
# Output:
# <Book: 1984 by George Orwell (1949)>
