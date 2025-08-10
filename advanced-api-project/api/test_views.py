from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create test user and author
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Test Author')
        
        # Create some books
        self.book1 = Book.objects.create(title='Book One', publication_year=2001, author=self.author)
        self.book2 = Book.objects.create(title='Book Two', publication_year=2002, author=self.author)

        # Initialize API client
        self.client = APIClient()


def test_list_books_unauthenticated(self):
    response = self.client.get('/books/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)

def test_create_book_unauthenticated(self):
    data = {
        'title': 'New Book',
        'publication_year': 2025,
        'author': self.author.id
    }
    response = self.client.post('/books/create/', data)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

def test_create_book_authenticated(self):
    self.client.login(username='testuser', password='testpass')
    data = {
        'title': 'New Book',
        'publication_year': 2025,
        'author': self.author.id
    }
    response = self.client.post('/books/create/', data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response.data['title'], 'New Book')


def test_update_book(self):
    self.client.login(username='testuser', password='testpass')
    url = f'/books/{self.book1.id}/update/'
    data = {
        'title': 'Updated Title',
        'publication_year': 2005,
        'author': self.author.id
    }
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.book1.refresh_from_db()
    self.assertEqual(self.book1.title, 'Updated Title')

def test_delete_book(self):
    self.client.login(username='testuser', password='testpass')
    url = f'/books/{self.book1.id}/delete/'
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

def test_filter_books_by_title(self):
    response = self.client.get('/books/?title=Book One')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['title'], 'Book One')

def test_search_books(self):
    response = self.client.get('/books/?search=Two')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['title'], 'Book Two')

def test_order_books_desc_publication_year(self):
    response = self.client.get('/books/?ordering=-publication_year')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    years = [book['publication_year'] for book in response.data]
    self.assertEqual(years, sorted(years, reverse=True))
