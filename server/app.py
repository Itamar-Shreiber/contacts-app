from flask import Flask
from flask_cors import CORS
from routes import contacts_blueprint

app = Flask(__name__) # יצירת מופע של אפליקציית Flask
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

# רישום ה־blueprint
app.register_blueprint(contacts_blueprint, url_prefix='/contacts')

#כשמריצים קובץ ישירות אז פייתון נותן לו את השם מיין. ולכן כאשר מריצים את הפקודה:
# python app.py אז:
#  __name__ יהיה __main__
if __name__ == '__main__': # הפעלת האפליקציה __name__ הוא '__main__' כאשר הקובץ רץ ישירות
    app.run(debug=True)
