from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# тест на добавление новой книги
    @pytest.mark.parametrize("book_name", [
        '1984',
        '451 градус по Фаренгейту',
        'Мастер и Маргарита'
    ])
    def test_add_new_book_success(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize("book_name, genre", [
        ('Мастер и Маргарита', 'Комедии'),
        ('451 градус по Фаренгейту', 'Фантастика')
    ])
    def test_set_book_genre_success(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize("book_name", [
        '451 градус по Фаренгейту',
        '1984'
    ])
    def test_get_book_genre_success(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_book_genre(book_name) == 'Фантастика'

    @pytest.mark.parametrize("book_name, genre", [
        ('Убить пересмешника', 'Детективы')
    ])
    def test_get_books_with_specific_genre_success(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    @pytest.mark.parametrize("book_name", [
        'Приключения Тома Сойера'
    ])
    def test_get_books_for_children_success(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert book_name in collector.get_books_for_children()

    @pytest.mark.parametrize("book_name", [
        'Властелин колец'
    ])
    def test_add_book_in_favorites_success(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("book_name", [
        'Гарри Поттер'
    ])
    def test_delete_book_from_favorites_success(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')  # Повторное добавление
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("book_name", [
        'Ужасы'
    ])
    def test_genre_age_rating_exclusion(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')
        assert book_name not in collector.get_books_for_children()

    @pytest.mark.parametrize("book_title", ['', 'A' * 101])
    def test_add_new_book_title_length_out_of_bounds(self, book_title):
        collector = BooksCollector()

        collector.add_new_book(book_title)

        assert book_title not in collector.get_books_genre()