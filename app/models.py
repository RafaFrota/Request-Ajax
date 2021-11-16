from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return Users.query.filter_by(id=user_id).first()

class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    #conf = relationship('Users', ForeignKey('user_id'))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def seleciona_usuario(self):
        usuario_objeto = Users.query.filter_by(id=id).first()
        #print(current_user.name)
        print(str(usuario_objeto.name))

class Config_ML(db.Model):
    __tablename__ = 'Config_ML'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('Users.id'), nullable=False)
    access_token = db.Column(db.String(76), nullable=False)
    token_type = db.Column(db.String(8), nullable=False)
    scope = db.Column(db.String(25), nullable=False)
    user_id_ML = db.Column(db.Integer)
    refresh_token = db.Column(db.String(38), nullable=False)
    

    def __init__(self, user_id, access_token,token_type, scope, user_id_ML, refresh_token):
        self.user_id = user_id
        self.access_token = access_token
        self.token_type = token_type
        self.scope = scope
        self.user_id_ML = user_id_ML
        self.refresh_token = refresh_token
        
    '''def __repr__(self):
        return '<Config %r>' % self.config_ML'''

    def __repr__(self):
        return str(self.access_token) + ", " + self.refresh_token

class Produto(db.Model):
    __tablename__ = 'Produto'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('Users.id'), nullable=False)
    nome = db.Column(db.String(76), nullable=False)
    qtd = db.Column(db.Integer, nullable=False)
    Descricao = db.Column(db.String(350), nullable=False)
    img = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, nome, qtd, Descricao, img):
        self.user_id = user_id
        self.nome = nome
        self.qtd = qtd
        self.Descricao = Descricao
        self.img = img
    '''def __repr__(self):
        return '<Config %r>' % self.config_ML'''

    def __repr__(self):
        return str(self.nome) + ", " + self.img

class Produto_ML(db.Model):
    __tablename__ = 'Produto_ML'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Produito_id = db.Column(db.Integer, ForeignKey('Produto.id'), nullable=False)
    json_ML = db.Column(db.String(250), nullable=False)

    def __init__(self, user_id, json_ML):
        self.Produito_id = user_id
        self.json_ML = json_ML
        
    '''def __repr__(self):
        return '<Config %r>' % self.config_ML'''

    def __repr__(self):
        return str(self.Produito_id) + ", " + self.json_ML
