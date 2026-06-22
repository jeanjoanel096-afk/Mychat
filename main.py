from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Baz done nan memwa sèvè a kote imel yo pral sèvi kòm idantifyan inik
users_db = {}

# Nou ka toujou kite yon kont tès si n vle, men kounye a moun ka enskri pou kont yo
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
    # Kounye a paj la ap louvri tou senp, se JavaScript lan k ap jere afichaj paj login lan an premye
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email', '').strip().lower()
    password = data.get('password', '').strip()
    username = data.get('username', '').strip()

    if not email or not password or not username:
        return jsonify({"success": False, "message": "Tanpri ranpli tout espas yo!"})

    # Tcheke si imel la deja itilize
    if email in users_db:
        return jsonify({"success": False, "message": "Imel sa a gen yon kont sou li deja!"})

    # Tcheke si non itilizatè a deja pran
    for u in users_db.values():
        if u['username'].lower() == username.lower():
            return jsonify({"success": False, "message": "Non itilizatè sa a deja pran!"})

    # Anrejistre nouvo itilizatè a
    users_db[email] = {
        "username": username,
        "password": password,
        "pwen": 0,
        "moncash": "",
        "lang": "ht",
        "tèm": "dark"
    }

    return jsonify({
        "success": True,
        "username": username,
        "pwen": 0,
        "moncash": "",
        "message": "Kont ou kreye ak siksè!"
    })

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
            "message": f"Byenvini ankò @{user_info['username']}!"
        })
    
    return jsonify({"success": False, "message": "Imel oswa modpas la pa kòrèk!"})

@app.route('/gade-piblisite', methods=['POST'])
def gade_piblisite():
    data = request.json
    username = data.get('username')

    # Chèche itilizatè a nan baz done a pa non l
    for email, user_info in users_db.items():
        if user_info['username'] == username:
            user_info['pwen'] += 10
            return jsonify({
                "success": True, 
                "message": "Ou gade piblisite a! +10 Pwen", 
                "nouvo_balans": user_info['pwen']
            })
            
    return jsonify({"success": False, "message": "Itilizatè pa jwenn"}), 404

@app.route('/withdrawal', methods=['POST'])
def withdrawal():
    data = request.json
    username = data.get('username')
    pwen_pou_retire = int(data.get('pwen', 0))

    for email, user_info in users_db.items():
        if user_info['username'] == username:
            current_pwen = user_info['pwen']
            # Chanje a 200 pwen pou limit la match ak HTML la
            if current_pwen >= pwen_pou_retire and pwen_pou_retire >= 200:
                user_info['pwen'] -= pwen_pou_retire
                return jsonify({
                    "success": True, 
                    "message": f"Demann retrè de {pwen_pou_retire} pwen voye sou MonCash avèk siksè!", 
                    "nouvo_balans": user_info['pwen']
                })
            elif pwen_pou_retire < 200:
                return jsonify({"success": False, "message": "Fòk ou gen omwen 200 pwen pou w fè yon retrè."})
            else:
                return jsonify({"success": False, "message": "Pwen ou yo pa ase."})

    return jsonify({"success": False, "message": "Itilizatè pa jwenn"}), 404

@app.route('/update-settings', methods=['POST'])
def update_settings():
    data = request.json
    username = data.get('username')
    lang = data.get('lang')
    tèm = data.get('tèm')
    moncash = data.get('moncash')

    for email, user_info in users_db.items():
        if user_info['username'] == username:
            if lang: user_info['lang'] = lang
            if tèm: user_info['tèm'] = tèm
            if moncash: user_info['moncash'] = moncash
            return jsonify({"success": True, "message": "Reglaj yo ajou!"})

    return jsonify({"success": False, "message": "Erè nan mizajou"})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
