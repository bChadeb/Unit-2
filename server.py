from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

@app.route('/')
def home():
    cupcakes = get_cupcakes("cupcakes.csv")
    order = get_cupcakes("orders.csv")
    order_total = round(sum([float(x["price"]) for x in order]), 2)
    return render_template('index.html', cupcakes=cupcakes, items_num=len(order), order_total=order_total)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    price = float(request.form.get('price'))
    flavor = request.form.get('flavor')
    frosting = request.form.get('frosting')
    filling = request.form.get('filling')
    
    cupcake = {
        'size': 'normal',
        'name': name,
        'price': price,
        'flavor': flavor,
        'frosting': frosting,
        'filling': filling,
        'sprinkles': []  
    }
    
    add_cupcake_dictionary("cupcakes.csv", cupcake)
    return redirect(url_for('order'))

@app.route('/cupcake/<name>')
def view_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    if cupcake:
        return render_template('cupcake.html', cupcake=cupcake)
    else:
        return "Cupcake not found", 404

@app.route('/add-cupcake/<name>')
def add_cupcake_to_order(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."

@app.route('/individual-cupcake/<name>')
def individual_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    
    if cupcake:
        return render_template("individual-cupcake.html", cupcake=cupcake)
    else:
        return "Sorry cupcake not found."

@app.route('/order')
def order():
    cupcakes = get_cupcakes("orders.csv")

    cupcakes_counted = []
    cupcake_set = set()

    for cupcake in cupcakes:
        cupcake_set.add((cupcake["name"], cupcake["price"], cupcakes.count(cupcake)))

    return render_template("order.html", cupcakes=cupcake_set)

if __name__ == '__main__':
    app.debug = True
    app.run(port=4444, host="localhost")
