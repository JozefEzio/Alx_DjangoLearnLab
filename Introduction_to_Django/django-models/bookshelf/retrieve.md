# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve a single book using get()
book = Book.objects.get(title="1984")
print(book)

# Output:
# <Book: 1984 by George Orwell (1949)>
