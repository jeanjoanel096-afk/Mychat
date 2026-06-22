from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Baz done fiktif pou tès la (Nan memwa sèvè a)
users_db = {
    "testuser": {
        "password": "123", 
        "pwen": 50, 
        "moncash": "50937654321",
        "lang": "ht",
        "tèm": "dark"
    }
}

@app.route('/')
def home():
    user_data = users_db["testuser"]
    return render_template('index.html', user=user_data, username="testuser")

@app.route('/gade-piblisite', methods=['POST'])
def gade_piblisite():
    data = request.json
    username = data.get('username')

    if username in users_db:
        users_db[username]['pwen'] += 10
        return jsonify({
            "success": True, 
            "message": "Ou gade piblisite a! +10 Pwen", 
            "nouvo_balans": users_db[username]['pwen']
        })
    return jsonify({"success": False, "message": "Itilizatè pa jwenn"}), 404

@app.route('/withdrawal', methods=['POST'])
def withdrawal():
    data = request.json
    username = data.get('username')
    pwen_pou_retire = int(data.get('pwen', 0))

    if username in users_db:
        current_pwen = users_db[username]['pwen']
        if current_pwen >= pwen_pou_retire and pwen_pou_retire >= 100:
            users_db[username]['pwen'] -= pwen_pou_retire
            return jsonify({
                "success": True, 
                "message": f"Demann retrè de {pwen_pou_retire} pwen voye sou MonCash avèk siksè!", 
                "nouvo_balans": users_db[username]['pwen']
            })
        elif pwen_pou_retire < 100:
            return jsonify({"success": False, "message": "Fòk ou gen omwen 100 pwen pou w fè yon retrè."})
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

    if username in users_db:
        if lang: users_db[username]['lang'] = lang
        if tèm: users_db[username]['tèm'] = tèm
        if moncash: users_db[username]['moncash'] = moncash
        return jsonify({"success": True, "message": "Reglaj yo ajou!"})

    return jsonify({"success": False, "message": "Erè nan mizajou"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
