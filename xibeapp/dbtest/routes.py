
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from xibeapp import db, bcrypt
from xibeapp.models import Post
from xibeapp.posts.forms import PostForm
from xibeapp.models import User, Venda, Produto, VendaItem

from flask import Blueprint


dbtests = Blueprint('dbtest', __name__)

@dbtests.route("/dbtest/test")
def reset_db():
    db.drop_all()
    db.create_all()

    hash_password = bcrypt.generate_password_hash('admin').decode('utf-8')
    usuario_1 = User(admin=1, cpf='30938773003', username='admin', email='admin@xibe.com', password=hash_password)

    hash_password2 = bcrypt.generate_password_hash('12345678').decode('utf-8')
    usuario_2 = User(username='User1', cpf='34613139040', email='user1@xibe.com', password=hash_password2)

    hash_password3 = bcrypt.generate_password_hash('123456789').decode('utf-8')
    usuario_3 = User(username='User2', cpf='11302007017', email='user2@xibe.com', password=hash_password3)

    produto_1 = Produto(descricao='Produto 01', titulo='titulo 01', valor=70.10, qtd=20)
    produto_2 = Produto(descricao='Produto 02', titulo='titulo 02', valor=45.80, qtd=10)
    produto_3 = Produto(descricao='Produto 03', titulo='titulo 03', valor=64.90, qtd=25)
    produto_4 = Produto(descricao='Produto 04', titulo='titulo 04', valor=37.70, qtd=22)
    produto_5 = Produto(descricao='Produto 05', titulo='titulo 05', valor=25.35, qtd=12)

    db.session.add(usuario_1)
    db.session.add(usuario_2)
    db.session.add(usuario_3)

    db.session.add(produto_1)
    db.session.add(produto_2)
    db.session.add(produto_3)
    db.session.add(produto_4)
    db.session.add(produto_5)

    db.session.commit()
    cliente_2 = User.query.get(2)
    cliente_3 = User.query.get(3)

    produto_1 = Produto.query.get(1)
    produto_2 = Produto.query.get(2)
    produto_3 = Produto.query.get(3)
    produto_4 = Produto.query.get(4)

    venda_1 = Venda(user_id=cliente_2.id, total=(produto_1.valor +  produto_2.valor))
    db.session.add(venda_1)
    venda_1 = Venda.query.get(1)
    item1 = VendaItem(id_venda=venda_1.id, id_produto=produto_1.id, valorunt=produto_1.valor, qtd=1, valor=produto_1.valor)
    item2 = VendaItem(id_venda=venda_1.id, id_produto=produto_2.id, valorunt=produto_2.valor, qtd=1, valor=produto_2.valor)
    db.session.add(item1)
    db.session.add(item2)

    venda_2 = Venda(user_id=cliente_3.id, total=(produto_3.valor +  produto_4.valor))
    db.session.add(venda_2)
    venda_2 = Venda.query.get(2)
    item3 = VendaItem(id_venda=venda_2.id, id_produto=produto_3.id, valorunt=produto_3.valor, qtd=1, valor=(produto_3.valor) )
    item4 = VendaItem(id_venda=venda_2.id, id_produto=produto_4.id, valorunt=produto_4.valor, qtd=1, valor=(produto_4.valor) )
    db.session.add(item3)
    db.session.add(item4)


    db.session.commit()
    flash('Your db has been re-created!', 'success')
    return redirect(url_for('main.home'))
