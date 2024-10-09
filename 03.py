import re

def normalize_phone(phone_number: str) -> str:
    # function take phone number in string of different formats and return normalized phone number in string

    normalized_phone = re.sub(r"[^\d]", '', phone_number)

    if normalized_phone.startswith('380'):
        normalized_phone = '+' + normalized_phone
    else:
        normalized_phone = '+38'+ normalized_phone
        
    return normalized_phone 


normalize_phone("38050-111-22-22")