from flask import Flask, render_template, request, jsonify
import os, re, datetime
import db
from models import Book

app = Flask(__name__)

# Create the database and table and insert some 
# test books into the database.
if not os.path.isfile('books.db'):
    db.connect()
    
@app.route("/")
def index():
    return render_template("index.html")

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else: 
        return False
        
@app.route("/request", methods=['POST'])
def postRequest():
    req_data = request.get_json()
    email = req_data['email']
    if not isValid(email):
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
def getRequest():
    content_type = request.headers.get('Content-Type')
    bks = [b.serialize() for b in db.view()]
    if content_type == 'application/json':
        json = request.json
        for b in bks:
            if b['id'] == int(json['id']):
                return jsonify({
                    'res': b,
                    'status': 200,
                    'msg': 'Success getting all books in library!'
                })
        return