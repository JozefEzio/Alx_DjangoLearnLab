from django.contrib import admin
from .models import Library, Librarian, Book, Author
# Register your models here.


admin.site.register(Librarian)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Author)