from flask import Flask
from flask_cors import CORS
from routes import contacts_blueprint

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

# רישום ה־blueprint
app.register_blueprint(contacts_blueprint, url_prefix='/contacts')

if __name__ == '__main__':
    app.run(debug=True)
