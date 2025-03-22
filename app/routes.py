from flask import Blueprint
from app.controllers.book_controller import get_categories, show_books_by_category, search, book_detail

books = Blueprint('books', __name__) 

@books.route('/', methods=['GET'])
def home():
    """En enkel startsida eller en välkomstmeddelande."""
    return "Välkommen till Bookstore API!"


@books.route('/categories', methods=['GET'])
def get_categories_route():
    return get_categories()

@books.route('/category/<category>', methods=['GET'])
def show_books_by_category_route(category):
    return show_books_by_category(category)

@books.route('/search', methods=['GET'])
def search_route():
    return search()

@books.route('/book/<int:book_id>', methods=['GET'])
def book_detail_route(book_id):
    return book_detail(book_id)





