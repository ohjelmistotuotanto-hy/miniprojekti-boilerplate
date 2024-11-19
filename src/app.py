from flask import redirect, render_template, request, jsonify
from db_helper import reset_db
from repositories.book_repository import get_books, create_book
from config import app, test_env

# Lataa nykyiset kirjat alkunäytölle
@app.route("/")
def index():
    books = get_books()
    print(books)
    return render_template("index.html", books=books)

@app.route("/new_book")
def new_book():
    return render_template("new_book.html")

# Luo kirjan databaseen riippuen syötteistä
@app.route("/create_book", methods=["GET","POST"])
def book_creation():
    author = request.form.get("author")
    title = request.form.get("title")
    publisher = request.form.get("publisher")
    year = request.form.get("year")
    create_book(author, title, publisher, year)
    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
