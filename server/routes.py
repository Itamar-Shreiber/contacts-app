from flask import Blueprint, jsonify, request
from db import get_connection

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
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone = data.get('phone')
    email = data.get('email')

    print(f"Creating contact - First name: {first_name}, Last name: {last_name}, Phone: {phone}, Email: {email}")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO contacts (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, phone, email)
        )
        conn.commit()
        print("Insert successful")
        response = jsonify({'message': 'Contact created'})
        response.status_code = 201
    except Exception as e:
        print(f"Error during insert: {e}")
        response = jsonify({'message': 'Error creating contact', 'error': str(e)})
        response.status_code = 500
    finally:
        cursor.close()
        conn.close()

    return response

# UPDATE
@contacts_blueprint.route('/<int:id>', methods=['PUT'])
def update_contact(id):
    data = request.json
    print(f"Received update request for contact id: {id}")
    print(f"Request JSON data: {data}")

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone = data.get('phone')
    email = data.get('email')
    print(f"Updating contact to - First name: {first_name}, Last name: {last_name}, Phone: {phone}, Email: {email}")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE contacts SET first_name=%s, last_name=%s, phone=%s, email=%s WHERE id=%s",
            (first_name, last_name, phone, email, id)
        )
        conn.commit()
        print("Update successful")
        response = jsonify({'message': 'Contact updated'})
        response.status_code = 200
    except Exception as e:
        print(f"Error during update: {e}")
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
