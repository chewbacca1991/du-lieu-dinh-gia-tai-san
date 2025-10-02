from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///real_estate.db'
db = SQLAlchemy(app)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    area = db.Column(db.Float, nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_sold = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Property {self.id}>'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Placeholder for the prediction logic
    return jsonify({'predicted_price': 100000})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
