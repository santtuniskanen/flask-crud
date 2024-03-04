"""
models.py defines the model for the books and has a function
to prepare the object to be made into json.
"""

class Book:
    """
    Represents a book object with attributes:
    ID, title, available and timestamp.
    """
    def __init__(self, book_id, available, title, timestamp):
        self.id = book_id
        self.title = title
        self.available = available
        self.timestamp = timestamp

    def __repr__(self):
        """
        returns a string representation of the book_id
        object.
        """
        return f'<id {self.id}>'

    def serialize(self):
        """
        converts the Book object into a dictionary.
        """
        return {
            'id': self.id,
            'title': self.title,
            'available': self.available,
            'timestamp': self.timestamp
        }
