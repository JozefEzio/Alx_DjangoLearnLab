from django.contrib import admin
from .models import Library, Librarian, Book, Author,UserProfile
# Register your models here.


admin.site.register(Librarian)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(UserProfile)