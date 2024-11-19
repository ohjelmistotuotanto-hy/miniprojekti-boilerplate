from sqlalchemy import text
from config import db


# Hakee kaikki kirjat ja niiden tiedot
def get_books():
    sql = text("SELECT id, author, title, publisher, year FROM books")
    result = db.session.execute(sql)
    all_books = result.fetchall()
    print(all_books)
    return all_books

def create_book(author, title, publisher, year):
    sql = text("INSERT INTO books (author, title, publisher, year) VALUES (:author, :title, :publisher, :year)")
    db.session.execute(sql, {"author":author, "title":title, "publisher":publisher, "year":year})
    db.session.commit()
    print("Luotu uusi")

