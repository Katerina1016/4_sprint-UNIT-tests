import pytest


class TestBooksCollector:
    def test_add_new_book_book_no_genre(self, books_collection):
        book_add = 'Золушка'
        books_collection.add_new_book(book_add)
        assert books_collection.get_book_genre(book_add) == ''

    @pytest.mark.parametrize('book', ['Всё или ничего, либо как нам быть в такой ситуации'])
    def test_add_new_book_book_with_name_large_number_of_characters(self, book, books_collection):
        books_collection.add_new_book(book)
        assert len(books_collection.get_books_genre()) == 0

    def test_set_book_genre_genre_added(self, books_collection):
        book = 'Оно'
        genre = 'Фантастика'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, genre)
        assert books_collection.get_book_genre(book) == genre

    def test_set_book_genre_genre_not_added(self, books_collection):
        book = 'История России'
        excluded_genre = 'Учебная'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, excluded_genre)
        assert books_collection.get_book_genre(book) == ''

    def test_get_books_with_specific_genre_no_such_genre(self, books_collection_five_books):
        assert len (books_collection_five_books.get_books_with_specific_genre('Поэзия')) == 0

    def test_get_books_for_children_no_age_restricted_books(self, books_collection_five_books):
        books_for_children = books_collection_five_books.get_books_for_children()
        assert len(books_for_children) == 1 and books_for_children == ['Оно']

    def test_add_book_in_favorite_name_book_in_favorite(self, books_collection):
        book = 'Оно'
        books_collection.add_new_book(book)
        books_collection.add_book_in_favorites(book)
        favorite_books = books_collection.get_list_of_favorites_books()
        assert len(favorite_books) == 1 and favorite_books[0] == book

    def test_delete_book_from_favorite_name_book_delete(self, books_collection):
        book = 'Оно'
        books_collection.add_new_book(book)
        books_collection.add_book_in_favorites(book)
        books_collection.delete_book_from_favorites(book)
        assert len(books_collection.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorite_books_not_list_not_added(self, books_collection):
        book = 'Еще'
        books_collection.add_book_in_favorites(book)
        assert len(books_collection.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorite_book_add_twice_not_added(self, books_collection):
        book = 'Учение свет'
        books_collection.add_new_book(book)
        books_collection.add_book_in_favorites(book)
        books_collection.add_book_in_favorites(book)
        favorite_books=books_collection.get_list_of_favorites_books()
        assert len(favorite_books) == 1 and favorite_books[0] == book