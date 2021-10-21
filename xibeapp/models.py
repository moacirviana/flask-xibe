from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from xibeapp import db, login_manager
from flask import current_app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(70), unique=True, nullable=False)
    picture = db.Column(db.String(20), nullable=False, default='food-silhouette.png')
    titulo = db.Column(db.String(120), unique=True, nullable=False)
    valor = db.Column(db.Float, nullable=False, default=0)
    qtd = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Produto('{self.titulo}', '{self.qtd}', '{self.valor}')"

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datacad = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    obs = db.Column(db.String(100), nullable=True)
    status = db.Column(db.Integer, nullable=False, default=0)
    total = db.Column(db.Float, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    itens = db.relationship('VendaItem', backref='items', lazy=True)

    def __repr__(self):
        return f"Venda('{self.id}', '{self.datacad}', '{self.status}')"
        
class VendaItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    id_venda = db.Column(db.Integer, db.ForeignKey('venda.id'), nullable=False)
    obs = db.Column(db.String(100), nullable=True)
    qtd = db.Column(db.Integer, nullable=False, default=0)
    valor = db.Column(db.Float, nullable=False, default=0)
    desconto = db.Column(db.Float, nullable=False, default=0)
    valorunt = db.Column(db.Float, nullable=False, default=0)
   
    def __repr__(self):
        return f"Items('{self.id_produto}', '{self.qtd}', '{self.valor}')"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    active = db.Column(db.Integer, default=0)
    admin = db.Column(db.Integer, default=0)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(20), unique=True, nullable=True)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Venda', backref='buyer', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
        
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"