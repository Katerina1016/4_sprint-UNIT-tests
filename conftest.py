import pytest
from main import BooksCollector

@pytest.fixture
def books_collection():
    books_collection = BooksCollector()
    return books_collection

@pytest.fixture
def books_collection_five_books(books_collection):
    collection = books_collection
    books = ['Призрак', 'Оно', 'Колобок', 'Любовь на всю голову', 'Литература']
    genre = ['Ужасы', 'Фантастика', 'Сказка', 'Роман', 'Учебная']
    for i in range(5):
        collection.add_new_book(books[i])
    for i in range(5):
        collection.set_book_genre(books[i], genre[i])
    return collection



