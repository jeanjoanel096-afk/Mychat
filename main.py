from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Baz done senp pou tès
user_data = {"username": "ProUser", "pwen": 0}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gade-piblisite', methods=['POST'])
def gade_piblisite():
    user_data['pwen'] += 10 # Ajoute 10 pwen
    return jsonify({"success": True, "nouvo_balans": user_data['pwen']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
