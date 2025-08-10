from django.db import models

# Create your models here.

class Author(models.Model):
    
    """
    Author model:
    - Represents an author entity in our library system.
    - Has a one-to-many relationship with Book (one author can have many books).
    """
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    
    """
    Book model:
    - Represents a single book.
    - Has a ForeignKey to Author, meaning each book is linked to one author.
    """
    title=models.CharField(max_length=100)
    publication_year=models.IntegerField()
    author=models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title} by {self.author}'