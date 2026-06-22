from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
# Yon ti baz done pou kòmanse
users_db = {"test@test.com": {"username": "ProUser", "pwen": 100, "moncash": "50900000000"}}

@app.route('/')
def home():
    # Menm si itilizatè a pa konekte, li voye done vid pou pa gen "Internal Server Error"
    return render_template('index.html', user={"pwen": 0, "username": "Guest"}, logged_in=False)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    # Lojik login la...
    return jsonify({"success": True, "message": "Konekte!", "pwen": 100})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
