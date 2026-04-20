from flask import Flask, render_template, request, redirect, url_for, flash
from models import init_db
from action_db import *

app = Flask(__name__)
app.secret_key = 'secret123'
init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').lower().strip()
        price = float(request.form.get('price', 0))
        category = request.form.get('category', '').lower().strip()
        if not product_exist(name):
            add_product(name, price, category)
        return redirect(url_for('index'))

    choice = request.args.get('category', 'all')
    if choice == 'all':
        products = Product.select()  # Прямий виклик ORM
    else:
        products = Product.select().where(Product.category == choice)

    categories = Product.select(Product.category).distinct()

    return render_template('index.html',
                           products=products,
                           categories=categories,
                           choice_category=choice)

@app.route('/delete/<name>')
def delete(name):
    delete_product_by_name(name)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)

#test