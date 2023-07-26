from datetime import datetime

province_list = {
    '11': 'Aceh',
    '12': 'Sumatera Utara',
    '13': 'Sumatera Barat',
    '16': 'Sumatera Selatan',
    '14': 'Riau',
    '21': 'Kepulauan Riau',
    '15': 'Jambi',
    '17': 'Bengkulu',
    '18': 'Lampung',
    '19': 'Bangka Belitung',
    '31': 'DKI Jakarta',
    '36': 'Banten',
    '32': 'Jawa Barat',
    '33': 'Jawa Tengah',
    '34': 'DI Yogyakarta',
    '35': 'Jawa Timur',
    '51': 'Bali',
    '61': 'Kalimantan Barat',
    '62': 'Kalimantan Tengah',
    '63': 'Kalimantan Selatan',
    '64': 'Kalimantan Timur',
    '65': 'Kalimantan Utara',
    '52': 'Nusa Tenggara Barat',
    '53': 'Nusa Tenggara Timur',
    '71': 'Sulawesi Utara',
    '72': 'Sulawesi Tengah',
    '73': 'Sulawesi Selatan',
    '74': 'Sulawesi Tenggara',
    '75': 'Gorontalo',
    '76': 'Sulawesi Barat',
    '81': 'Maluku',
    '82': 'Maluku Utara',
    '91': 'Papua',
    '92': 'Papua Barat'
}


def get_id_info(x: str):
    """
    Parses an Indonesian ID card number and returns a list of its components.

    Args:
    x (str): The ID card number to be parsed. Must be 16 characters long.

    Returns:
    list: A list containing the following components of the ID card number:
        - The province code (2 characters)
        - The province name
        - The city code (4 characters)
        - The district code (6 characters)
        - The gender ('MALE' or 'FEMALE')
        - The birth year (4 digits)
        - The age (in years)

    If the input is not 16 characters long, returns a list of None values.
    """
    # implementation of the function
    
    if len(x) != 16:
        return [None, None, None, None, None, None, None]

    id_province = x[:2]
    id_city = x[:4]
    id_district = x[:6]

    if int(x[6:8]) > 31:
        id_gender = 'FEMALE'
    else:
        id_gender = 'MALE'

    if int(x[-6]) == 0 or int(x[-6]) == 1:
        id_birthyear = int('20' + x[-6:-4])
    else:
        id_birthyear = int('19' + x[-6:-4])

    current_year = datetime.now().year
    id_age = current_year - id_birthyear
    province_name = province_list.get(id_province)

    return [province_name, id_city, id_district, id_gender, id_birthyear, id_age]


if __name__ == '__main__':
    while True:
        id_card_number = input("Enter an Indonesian ID card number (16 digits): ")
        if len(id_card_number) != 16:
            print("Invalid input. Please enter a 16-digit ID card number.")
            continue
        parsed_id_card = get_id_info(id_card_number)
        if None in parsed_id_card:
            print("Invalid ID card number. Please enter a valid 16-digit ID card number.")
            continue
        age = parsed_id_card[-1]
        gender = parsed_id_card[3]        
        print(f'Age: {age}, Gender: {gender}')
        break
