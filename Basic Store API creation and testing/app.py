from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name' : 'my item',
                'price' : 100
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')


# POST /store/data: {data}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)



# Get /store/<string:name>
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    # iterate over store
    for store in stores:
        if store['name'] == name:
            return jsonify(store)

    return jsonify({'Message' : 'Store not found'})



# Get /store/
@app.route('/store')
def get_stores():
    return jsonify({'stores' : stores}) 



# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

    return jsonify({'Message' : 'Store already exists'}) 



# GET /store/<string:name>/item 
@app.route('/store/<string:name>/item')  # 'http://127.0.0.1:5000/store/some_name'
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})

    return jsonify({'Message' : 'Store not found'})


app.run(port=5000)