import sqlite3
from flask import jsonify, request

def get_db_connection():
    """Ansluter till SQLite-databasen och returnerar anslutningen."""
    conn = sqlite3.connect('books_data.db') 
    conn.row_factory = sqlite3.Row  
    return conn


def get_categories():
    """Hämtar alla bokkategorier från databasen och returnerar som JSON."""
    conn = get_db_connection()
    categories = conn.execute('SELECT DISTINCT book_category FROM books').fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in categories])


def show_books_by_category(category):
    """Visar böcker från en specifik kategori."""
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books WHERE book_category = ?', (category,)).fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in books])


def search():
    """Söker böcker baserat på användarens sökfråga."""
    query = request.args.get('q', '')
    conn = get_db_connection()
    books = conn.execute("SELECT * FROM books WHERE book_title LIKE ?", ('%' + query + '%',)).fetchall()
    conn.close()

    return jsonify([dict(row) for row in books])


def book_detail(book_id):
    """Visar detaljer om en bok baserat på dess ID."""
    conn = get_db_connection()
    book = conn.execute("SELECT * FROM books WHERE book_id = ?", (book_id,)).fetchone()
    conn.close()

    if book is None:
        return jsonify({"error": "Boken hittades inte"}), 404

    return jsonify(dict(book))
