"""
db.py handles database connection and the sql methods for crud functions.
"""

import sqlite3
import random
import datetime
from models import Book


def get_new_id():
    """
    get_new_id() randomly generates an id of type Int, which is 9 digits in long.
    """
    return random.getrandbits(28)


books = [
    {
        'available': True,
        'title': 'A Tale of Two Cities',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'The Lord of the Rings',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'The Little Prince',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': "Harry Potter and the Sorcerer's Stone",
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'And Then There Were None',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'The Dream of the Red Table',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'The Hobbit',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'The Lion, the Witch and the Wardrobe',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'The Da Vinci Code',
        'timestamp': datetime.datetime.now()
    },
]

def connect():
    """
    connect() connects to the sqlite database and creates
    a table "books" if it doesn't exist yet.
    """
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books "
            "(id INTEGER PRIMARY KEY, "
            "available BOOLEAN, "
            "title TEXT, "
            "timestamp TEXT)")
    conn.commit()
    conn.close()
    for i in books:
        bk = Book(get_new_id(), i['available'], i['title'], i['timestamp'])
        insert(bk)

def insert(book):
    """
    insert(book) inserts a book into the table given correct params.
    """
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (?,?,?,?)", (
        book.id,
        book.available,
        book.title,
        book.timestamp
    ))
    conn.commit()
    conn.close()

def view():
    """
    view() returns all books from the table.
    """
    conn = sqlite3.connect('books.db')
    cur  = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    book_list = []
    for i in rows:
        book = Book(i[0], i[1] == 1, i[2], i[3])
        book_list.append(book)
    conn.close()
    return book_list

def update(book):
    """
    Updates a book in the table given correct params.
    """
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE books "
            "SET available=?, "
            "title=? "
            "WHERE id=?",
            (book.available, book.title, book.id))
    conn.commit()
    conn.close()

def delete(the_id):
    """
    deletes a book from the table given id.
    """
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (the_id,))
    conn.commit()
    conn.close()

def delete_all():
    """
    deletes all books from the table.
    """
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books")
    conn.commit()
    conn.close()
    