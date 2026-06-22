from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Baz done nan memwa sèvè a
users_db = {}

# Kont tès pou sekirite
users_db["test@gmail.com"] = {
    "username": "testuser",
    "password": "123", 
    "pwen": 50, 
    "moncash": "50937654321",
    "lang": "ht",
    "tèm": "dark"
}

@app.route('/')
def home():
    # Nou pase yon ti donte fiktif vid pou HTML la pa fè erè lè l ap chaje an premye
    empty_user = {"pwen": 0, "moncash": "", "lang": "ht", "tèm": "dark"}
    return render_template('index.html', user=empty_user, username="")

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email', '').strip().lower()
    password = data.get('password', '').strip()
    username = data.get('username', '').strip()

    if not email or not password or not username:
        return jsonify({"success": False, "message": "Tanpri ranpli tout espas yo!"})

    if email in users_db:
        return jsonify({"success": False, "message": "Imel sa a deja gen yon kont!"})

    for u in users_db.values():
        if u['username'].lower() == username.lower():
            return jsonify({"success": False, "message": "Non itilizatè sa a deja pran!"})

    users_db[email] = {
        "username": username,
        "password": password,
        "pwen": 0,
        "moncash": "",
        "lang": "ht",
        "tèm": "dark"
    }

    return jsonify({"success": True, "username": username, "message": "Kont ou kreye ak siksè!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email', '').strip().lower()
    password = data.get('password', '').strip()

    if email in users_db and users_db[email]['password'] == password:
        user_info = users_db[email]
        return jsonify({
            "success": True,
            "username": user_info['username'],
            "pwen": user_info['pwen'],
            "moncash": user_info['moncash'],
            "message": "Byenvini ankò!"
        })
    
    return jsonify({"success": False, "message": "Imel oswa modpas la pa kòrèk!"})

@app.route('/gade-piblisite', methods=['POST'])
def gade_piblisite():
    data = request.json
    username = data.get('username')
    for email, user_info in users_db.items():
        if user_info['username'] == username:
            user_info['pwen'] += 10
            return jsonify({"success": True, "message": "+10 Pwen!", "nouvo_balans": user_info['pwen']})
    return jsonify({"success": False, "message": "Itilizatè pa jwenn"}), 404

@app.route('/withdrawal', methods=['POST'])
def withdrawal():
    data = request.json
    username = data.get('username')
    pwen_pou_retire = int(data.get('pwen', 0))
    for email, user_info in users_db.items():
        if user_info['username'] == username:
            if user_info['pwen'] >= pwen_pou_retire and pwen_pou_retire >= 200:
                user_info['pwen'] -= pwen_pou_retire
                return jsonify({"success": True, "message": "Demann voye!", "nouvo_balans": user_info['pwen']})
            return jsonify({"success": False, "message": "Fòk ou gen omwen 200 pwen."})
    return jsonify({"success": False, "message": "Itilizatè pa jwenn"}), 404

@app.route('/update-settings', methods=['POST'])
def update_settings():
    data = request.json
    username = data.get('username')
    for email, user_info in users_db.items():
        if user_info['username'] == username:
            if data.get('lang'): user_info['lang'] = data.get('lang')
            if data.get('tèm'): user_info['tèm'] = data.get('tèm')
            if data.get('moncash'): user_info['moncash'] = data.get('moncash')
            return jsonify({"success": True, "message": "Reglaj yo ajou!"})
    return jsonify({"success": False, "message": "Erè nan mizajou"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
