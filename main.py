from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
users_db = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email, username = data.get('email'), data.get('username')
    users_db[email] = {"username": username, "pwen": 0}
    return jsonify({"success": True, "username": username, "pwen": 0})

@app.route('/gade-piblisite', methods=['POST'])
def gade():
    data = request.json
    username = data.get('username')
    for email in users_db:
        if users_db[email]['username'] == username:
            users_db[email]['pwen'] += 10
            return jsonify({"success": True, "nouvo_balans": users_db[email]['pwen']})
    return jsonify({"success": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
