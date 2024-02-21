'''
from flask import Flask,request,jsonify

app=Flask(__name__)

book_list=[
    {
        'id':0,
        "author":"chinnu achae",
        "language": "english",
        "title": "Thing Fall Apart",
    },
    {
        'id': 1,
        "author": "hans chrisitan Andersen",
        "language": "Danish",
        "title": "Fairy Tales",
    },  {
        'id':2,
        "author":"Robert",
        "language": "english",
        "title": "Crime ",
    },
    {
        'id': 3,
        "author": "yusuku",
        "language": "japense",
        "title": "moutain ",
    },
    {
        'id': 3,
        "author": "yusuku",
        "language": "japense",
        "title": "moutain ",
    },
    {
        'id': 3,
        "author": "yusuku",
        "language": "japense",
        "title": "moutain ",
    },
    {
        'id': 4,
        "author": "bathuru",
        "language": "japense",
        "title": "moutain ",
    }

]


@app.route("/books",methods=['GET','POST'])
def books():
    if request.method == "GET":
        if len(book_list)>0:
            return jsonify(book_list)
        else:
            'Nothing Found',404

    if request.method == "POST":
        new_author = request.form['author']
        new_lang=request.form['language']
        new_title=request.form['title']
        iD=book_list[-1]['id']+1

        new_obj={
            'id':iD,
            'author':new_author,
            'language':new_lang,
            'title':new_title
        }

        book_list.append(new_obj )
        return  jsonify(book_list)

@app.route('/books/<int:id>',methods=['GET','PUT','DELETE'])

def single_book(id):

    if request.method == 'GET':
        for book in book_list:
            if book['id'] == id:
                return  jsonify(book)
                pass
                
    if request.method == 'PUT':
        for book in book_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                updated_book ={
                    'id': id,
                    'author': book['author'],
                    'language': book['language'],
                    'title': book['title']
                }
                return  jsonify(updated_book)

    if request.method == 'DELETE':
        for index,book in enumerate (book_list):
            if book['id'] == id:
                book_list.remove(index)
            return jsonify(book_list)

if __name__ == '__main__':
    app.run(debug=True)
'''


"""
#final code ------------------------------------------------>>>>>>>>>>>>
from flask import Flask, request, jsonify

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
        return jsonify(book_list)
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
    return jsonify(book_list)


@app.route('/books/<int:id>', methods=['GET'])
def get_single_book(id):
    for book in book_list:
        if book['id'] == id:
            return jsonify(book)
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
            return jsonify(updated_book)
    return 'Book not found'


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_single_book(id):
    for book in book_list:
        if book['id'] == id:
            book_list.remove(book)
            return jsonify(book_list)
    return 'Book not found'


if __name__ == '__main__':
    app.run(debug=True)
    #=------------------------------------------------------------>
"""



'''
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
    new_author = request.json['author']
    new_lang = request.json['language']
    new_title = request.json['title']
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
            book['author'] = request.json['author']
            book['language'] = request.json['language']
            book['title'] = request.json['title']
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
'''


'''
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
    
'''



#app staic final without db

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
        return json.dumps(book_list,indent=4)  # Serialize to JSON using dumps
    else:
        return 'Nothing Found'

@app.route("/books", methods=['POST'])
def create_book():
    new_author = request.json['author']
    new_lang = request.json['language']
    new_title = request.json['title']
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
            book['author'] = request.json['author']
            book['language'] = request.json['language']
            book['title'] = request.json['title']
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

