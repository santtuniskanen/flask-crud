"""
app.py contains the initialization for the Flask application.
It also contains the endpoints and crud methods for the book application.
"""

import os
import re
import datetime
from flask import Flask, render_template, request, jsonify
import db
from models import Book

app = Flask(__name__)

# Create the database and table and insert some
# test books into the database.
if not os.path.isfile('books.db'):
    db.connect()

@app.route("/")
def index():
    """
    returns the index.html template.
    """
    return render_template("index.html")

def is_valid(email):
    """
    uses regular expressions to validate email input, not sure for what reason.
    There is no email input anywhere in this application.
    """
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    return False

@app.route("/request", methods=['POST'])
def post_request():
    """
    post_request()
    """
    req_data = request.get_json()
    email = req_data['email']
    if not is_valid(email):
        return jsonify({
            'status': '422',
            'res': 'failure',
            'error': 'Invalid email format. Please enter a valid email address'
        })
    title = req_data['title']
    bks = [b.serialize() for b in db.view()]
    for b in bks:
        if b['title'] == title:
            return jsonify({
                'res': f'Error! Book with title {title} is already in library!',
                'status': '404'
            })

    bk = Book(db.getNewId(), True, title, datetime.datetime.now())
    print('new book', bk.serialize())
    db.insert(bk)
    new_bks = [b.serialize() for b in db.view()]
    print('books in lib: ', new_bks)

    return jsonify({
                'res': bk.serialize(),
                'status': '200',
                'msg': 'Success creating a new book!'
    })

@app.route('/request', methods=['GET'])
def get_request():
    """
    get_request() returns everything from the books table.
    """
    content_type = request.headers.get('Content-Type')
    bks = [b.serialize() for b in db.view()]
    if content_type == 'application/json':
        json = request.json
        for b in bks:
            if b['id'] == int(json['id']):
                return jsonify({
                    'res': b,
                    'status': '200',
                    'msg': 'Success getting all books in library!'
                })
        return jsonify({
            'error': f"Error! Book with id '{json['id']}' not found!",
            'res': '',
            'status': '404'
        })

    return jsonify({
                'res': bks,
                'status': '200',
                'msg': 'Success getting all books in library!',
                'no_of_books': len(bks)
            })

@app.route('/request/<id>', methods=['GET'])
def get_request_id(id):
    """
    get_request_id() returns a singular item from the books table given the correct id.
    """
    req_args = request.view_args
    bks = [b.serialize() for b in db.view()]
    if req_args:
        for b in bks:
            if b['id'] == int(req_args['id']):
                return jsonify({
                    'res': b,
                    'status': '200',
                    'msg': 'Success getting book by ID!'
                })
        return jsonify({
            'error': f"Error! Book with id '{req_args['id']}' was not found!",
            'res': '',
            'status': '404'
        })
    return jsonify({
                'res': bks,
                'status': '200',
                'msg': 'Success getting book by ID!',
                'no_of_books': len(bks)
            })

@app.route("/request", methods=['PUT'])
def put_request():
    """
    put_request()
    """
    req_data = request.get_json()
    availability = req_data['available']
    title = req_data['title']
    the_id = req_data['id']
    bks = [b.serialize() for b in db.view()]
    for b in bks:
        if b['id'] == the_id:
            bk = Book(
                the_id,
                availability,
                title,
                datetime.datetime.now()
            )
            print('new book: ', bk.serialize())
            db.update(bk)
            new_bks = [b.serialize() for b in db.view()]
            print('books in lib: ', new_bks)
            return jsonify({
                'res': bk.serialize(),
                'status': '200',
                'msg': f'Success updating the book titled {title}!👍😀'
            })
    return jsonify({
                'res': f'Error! Failed to update Book with title: {title}!',
                'status': '404'
            })

@app.route('/request/<id>', methods=['DELETE'])
def delete_request(id):
    """
    delete_request()
    """
    req_args = request.view_args
    print('req_args: ', req_args)
    bks = [b.serialize() for b in db.view()]
    print('bks: ', bks)
    if req_args:
        for b in bks:
            if b['id'] == int(req_args['id']):
                db.delete(b['id'])
                updated_bks = [b.serialize() for b in db.view()]
                print('updated_bks: ', updated_bks)
                return jsonify({
                    'res': updated_bks,
                    'status': '200',
                    'msg': 'Success deleting book by ID!',
                    'no_of_books': len(updated_bks)
                })
    return jsonify({
        'error': 'Error! No Book ID sent!',
        'status': '404'
    })

if __name__ == '__main__':
    app.run()
