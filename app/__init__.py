from flask import Flask
from app.routes import books  # Importera blueprint från routes.py

def create_app():
    """Skapar en Flask-applikation och registrerar en blueprint för att hantera rutter. 
    Returnerar den konfigurerade Flask-applikationen."""
    app = Flask(__name__)
    
    app.register_blueprint(books)

    return app