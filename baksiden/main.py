from flask import request, jsonify
from config import app, db
from models import Contact

# GET
@app.route("/contacts", method=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = map(lambda x: x.to_json(), contacts)
    return jsonify({"contacts": json_contacts})

if __name__ == '__main__':
    # Instantiate DB
    with app.app_context():
        db.create_all()

    app.run(debug=True)