from flask import render_template

from app.product import bp
from app.extensions import db
from app.models.product import Product

@bp.route('/price/<int:id>/')
def product_view(id):
    print(id)
    product = db.session.query(Product).filter(Product.id==id).first()
    return render_template("product.html", product=product)

