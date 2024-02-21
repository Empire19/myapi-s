from flask import Flask ,jsonify,request


app= Flask(__name__)



book_list=[
    {
        'id':0,
        "author":"chinnu achae",
        "language": "english",
        "title": "Thing Fall Apart"
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
]
@app.route("/get",methods=['GET'])
def get():
    if (request.method=='GET'):
        return jsonify(book_list)

@app.route("/post",methods=["POST"])
def post():
    if(request.method=='POST'):
        iD = book_list[-1]['id'] + 1
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']


        new_obj = {
            'id': iD,
            'author': new_author,
            'language': new_lang,
            'title': new_title
        }

        book_list.append(new_obj)
        return jsonify(book_list)
'''

@app.route("/put/<int:id>",methods=["PUT"])
def update():
    if(request.method=='PUT'):
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



'''

if __name__ == '__main__':
    app.run(debug=True)


