# validation.py

def validate_contact_data(data):
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone = data.get('phone')
    email = data.get('email')

    if not first_name or not last_name:
        return False, 'יש להזין שם פרטי ושם משפחה'

    if not phone or not phone.isdigit() or len(phone) < 7:
        return False, 'מספר טלפון לא תקין'

    if not email or '@' not in email:
        return False, 'כתובת אימייל לא תקינה'

    return True, None
