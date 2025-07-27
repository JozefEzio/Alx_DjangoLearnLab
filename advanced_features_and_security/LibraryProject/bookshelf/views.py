from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
# Create your views here.

"""
Permissions & Groups Setup Guide:

Custom Permissions (in Book model):
- can_view: Can view book list
- can_create: Can add books
- can_edit: Can update/edit books
- can_delete: Can delete books

Groups:
- Viewers: Assigned can_view
- Editors: Assigned can_view, can_create, can_edit
- Admins: Assigned all permissions

Usage:
- Views are protected with @permission_required
- Users must be in a group with the appropriate permission
"""



@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
