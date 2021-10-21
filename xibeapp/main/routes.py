from flask import render_template, request, Blueprint
from xibeapp.models import Venda

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    vendas = Venda.query.order_by(Venda.datacad.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', vendas=vendas)


@main.route("/about")
def about():
    return render_template('about.html', title='About')