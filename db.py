import sqlite3, random, datetime
from models import Book


def getNewId():
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