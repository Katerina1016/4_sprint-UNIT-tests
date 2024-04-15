import pytest
from main import BooksCollector
class TestBooksCollector:
    @pytest.mark.parametrize("name", [
        "Дюна",
        "Красная шапочка"])
    def test_add_new_book_valid_number_of_characted_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre


    def test_set_book_genre_book_have_no_genre(self):
        collector = BooksCollector()
        name = "Зеленая миля"
        collector.add_new_book(name)
        assert collector.books_genre[name] == ""

    def test_get_book_genre_book_not_list_no_genre(self):
        collector = BooksCollector()
        assert collector.get_book_genre("Оно") is None

    @pytest.mark.parametrize('name, genre', [
        ('Снежная королева', 'Сказка'),
        ('Оно', 'Ужасы'),
        ('Призрак', 'Ужасы'),
        ('Колобок', 'Сказка'),
        ('Любовь на всю голову', 'Роман')
    ])
    def test_get_books_with_specific_genre_fiction(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        book_with_genre = collector.get_books_with_specific_genre('Сказка')
        assert 'Снежная королева', 'Колобок' in books_with_genre

    @pytest.mark.parametrize('name, genre', [
        ('Пятачок', 'Сказка'),
        ('Страх', 'Ужасы'),
        ('Фунтик', 'Сказка'),
        ('Горячая кровь', 'Роман')
    ])
    def test_get_books_genre_dictionary(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert isinstance(collector.get_books_genre(), dict)

    @pytest.mark.parametrize('name, genre', [
        ('Пятачок', 'Сказка'),
        ('Страх', 'Ужасы'),
        ('Фунтик', 'Сказка'),
        ('Горячая кровь', 'Роман')
    ])
    def test_get_books_for_children_no_age_restricted_books_for_kids(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        book_for_children = collector.get_books_for_children()
        assert 'Страх' not in book_for_children

    def test_add_book_in_favorite_name_book_in_favorite(self):
        collector = BooksCollector()
        name = 'Оно'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    def test_delete_book_from_favorite_name_book_delete(self):
        collector = BooksCollector()
        name = 'Оно'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    @pytest.mark.parametrize('name', [
        'Жуть',
        'Золушка'
    ])
    def test_get_list_of_favorite_books_list_output(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        favorite_books = collector.get_list_of_favorites_books()
        assert name in favorite_books
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()