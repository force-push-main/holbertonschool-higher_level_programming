from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        items = json.load(f)
        return render_template('items.html', items=items)

@app.route('/products')
def products():
    if request.args.get('source') == 'json':
        data = []
        with open('products.json', 'r') as f:
            data = json.load(f)
        if request.args.get('id'):
            data = [row for row in data if row['id'] == int(request.args.get('id'))]
        if len(data) == 0:
            return render_template('product_display.html', data='no product')
        return render_template('product_display.html', data=data)
    if request.args.get('source') == 'csv':
        matrix = []
        with open('products.csv', mode='r', newline='') as f:
            data = csv.DictReader(f)
            matrix = [row for row in data]
        if request.args.get('id'):
            matrix = [row for row in matrix if row['id'] == request.args.get('id')]
        if len(matrix) == 0:
            return render_template('product_display.html', data='no product')
        return render_template('product_display.html', data=matrix)
    return render_template('product_display.html', data='error')

if __name__ == '__main__':
    app.run(debug=True, port=5000)