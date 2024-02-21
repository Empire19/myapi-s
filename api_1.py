'''
#GET , POST
from flask import Flask,request,jsonify
import json


app = Flask(__name__)

data=[]

@app.route('/',methods=['GET','POST'])
def author():
    if request.method == 'GET':

        return jsonify(data)
    if request.method == "POST":
        try:
            new_dic=json.loads(request.data)
            data.append(new_dic)
            return jsonify(new_dic),201
        except json.JSONDecodeError:
            return 'invalid json data',400


if __name__ == '__main__':
    app.run(debug=True)



'''
# using CRUD form method
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

book_list = [
   {
        'id': 1,
        "author": "hans chrisitan Andersen",
        "language": "Danish",
        "title": "Fairy Tales",
    },
    {
        'id': 2,
        "author": "Robert",
        "language": "english",
        "title": "Crime ",
    },
    {
        'id': 3,
        "author": "yusuku",
        "language": "chinese",
        "title": "moutain ",
    },
    {
        'id': 4,
        "author": "hilter",
        "language": "german",
        "title": "world war 2",
    },
    {
        'id': 5,
        "author": "alex",
        "language": "hindi",
        "title": "freedom",
    }
]

@app.route("/books", methods=['GET'])
def get_books():
    if len(book_list) > 0:
        return json.dumps(book_list)  # Serialize to JSON using dumps
    else:
        return 'Nothing Found'

@app.route("/books", methods=['POST'])
def create_book():
    new_author = request.form['author']
    new_lang = request.form['language']
    new_title = request.form['title']
    iD = book_list[-1]['id'] + 1

    new_obj = {
        'id': iD,
        'author': new_author,
        'language': new_lang,
        'title': new_title
    }

    book_list.append(new_obj)
    return json.dumps(book_list)  # Serialize to JSON using dumps

@app.route('/books/<int:id>', methods=['GET'])
def get_single_book(id):
    for book in book_list:
        if book['id'] == id:
            return json.dumps(book)  # Serialize to JSON using dumps
    return 'Book not found'

@app.route('/books/<int:id>', methods=['PUT'])
def update_single_book(id):
    for book in book_list:
        if book['id'] == id:
            book['author'] = request.form['author']
            book['language'] = request.form['language']
            book['title'] = request.form['title']
            updated_book = {
                'id': id,
                'author': book['author'],
                'language': book['language'],
                'title': book['title']
            }
            return json.dumps(updated_book)  # Serialize to JSON using dumps
    return 'Book not found'

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_single_book(id):
    for book in book_list:
        if book['id'] == id:
            book_list.remove(book)
            return json.dumps(book_list)  # Serialize to JSON using dumps
    return 'Book not found'

if __name__ == '__main__':
    app.run(debug=True)



