from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Baz done pou estati ak foto
db = {"status": "Aktif", "photos": []}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload-photo', methods=['POST'])
def upload_photo():
    if 'photo' in request.files:
        file = request.files['photo']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            db['photos'].append(file.filename)
            return jsonify({"success": True})
    return jsonify({"success": False})

@app.route('/get-data')
def get_data():
    return jsonify(db)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER): os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=10000)
