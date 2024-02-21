from flask import Flask,request,jsonify #jsonify,request method 
from flask_sqlalchemy import SQLAlchemy  # to do database by code
from flask_marshmallow import Marshmallow #data serialization
import os


### --------------------------------- APP CONFIGURATION -----------------------------------------------------###

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))  # this use for current location directory of your file
# print(basedir)


app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #any modification done app that track

# declare object-----------
db = SQLAlchemy(app)
ma = Marshmallow(app)

#Create Table--------------------
class user(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    contact = db.Column(db.String(100),unique=True)
    
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact

     
   
   
 #for Serialzation using marshmallow,acess from outer       
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','name','contact')
        
user_schema = UserSchema()   #object name
users_schema = UserSchema(many=True)  #many for multiple data


#for Creating in DB Browser
# with app.app_context():
#     db.create_all()

#Create Method
@app.route('/post',methods=['POST'])
def home(): 
   name =request.json['name']
   contact=request.json['contact']
   new_user =user(name,contact)    #create object for user table
   db.session.add(new_user)
   db.session.commit()
   return user_schema.jsonify(new_user)   #call user_schema
   
@app.route('/user',methods=['GET'])
def showuser():
    all_users=user.query.all()
    result=users_schema.dump(all_users)
    return jsonify(result)

@app.route('/user/<id>',methods=['GET'])
def getuserbyid(id):
    userid=user.query.get(id)
    return user_schema.jsonify(userid)


#update

@app.route('/user/<id>',methods=['PUT'])
def updateuser(id):
    userid=user.query.get(id)
    name = request.json['name']
    contact = request.json['contact']
    userid.name = name
    userid.contact =contact
    db.session.commit()
    return user_schema.jsonify(userid)

#Delete

@app.route('/user/<id>',methods=['DELETE'])

def deleteuser(id):
        userid=user.query.get(id)
        db.session.delete(userid)
        db.session.commit()
        return user_schema.jsonify(userid)




    
#run code
if __name__ == '__main__':
    app.run(debug=True)
    
