from flask import Blueprint, jsonify, request
from db import get_connection
from validation import validate_contact_data

contacts_blueprint = Blueprint('contacts', __name__)

@contacts_blueprint.route('/', methods=['GET'])
def get_contacts():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(results)

# CREATE
@contacts_blueprint.route('/', methods=['POST'])
def create_contact():
    data = request.json

    is_valid, error_msg = validate_contact_data(data)
    if not is_valid:
        return jsonify({'message': error_msg}), 400

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone = data.get('phone')
    email = data.get('email')

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO contacts (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, phone, email)
        )
        conn.commit()
        response = jsonify({'message': 'Contact created'})
        response.status_code = 201
    except Exception as e:
        response = jsonify({'message': 'Error creating contact', 'error': str(e)})
        response.status_code = 500
    finally:
        cursor.close()
        conn.close()

    return response

@contacts_blueprint.route('/<int:id>', methods=['PUT'])
def update_contact(id):
    data = request.json

    is_valid, error_msg = validate_contact_data(data)
    if not is_valid:
        return jsonify({'message': error_msg}), 400

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone = data.get('phone')
    email = data.get('email')

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE contacts SET first_name=%s, last_name=%s, phone=%s, email=%s WHERE id=%s",
            (first_name, last_name, phone, email, id)
        )
        conn.commit()
        response = jsonify({'message': 'Contact updated'})
        response.status_code = 200
    except Exception as e:
        response = jsonify({'message': 'Error updating contact', 'error': str(e)})
        response.status_code = 500
    finally:
        cursor.close()
        conn.close()

    return response

# DELETE
@contacts_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_contact(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Contact deleted'})
