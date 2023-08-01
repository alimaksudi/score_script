from datetime import datetime

# A dictionary that maps province codes to province names
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

# A dictionary that maps province codes to province groups
province_group_code = {
    'group_1': ['31', '36', '34', '33', '35', '18', '62', '73', '76', '53', '81'],
    'group_2': ['32', '17', '15', '16', '19', '72', '74', '52', '51'],
    'group_3': ['11', '12', '13', '14', '63', '61', '64', '71', '75', '91', '82']
}

def get_province_group(province_code):
    """
    Returns the group name of a given province code.

    Args:
    province_code (str): The province code to be checked. Must be 2 characters long.

    Returns:
    str: The name of the group that the province belongs to.
    """
    for group_name, group_codes in province_group_code.items():
        if province_code in group_codes:
            return group_name
    return None


def get_id_info(x: str):
    """
    Parses an Indonesian ID card number and returns a dictionary of its components.

    Args:
    x (str): The ID card number to be parsed. Must be 16 characters long.

    Returns:
    dict: A dictionary containing the following components of the ID card number:
        - The province code (2 characters)
        - The province name
        - The city code (4 characters)
        - The district code (6 characters)
        - The gender ('MALE' or 'FEMALE')
        - The birth year (4 digits)
        - The age (in years)

    If the input is not 16 characters long, returns a dictionary of None values.
    """
    # Initialize an empty dictionary to store the parsed components
    id_info = {}

    if len(x) != 16:
        # If the input is not 16 characters long, return a dictionary of None values
        id_info = {
            'province_code': None,
            'province_name': None,
            'city_code': None,
            'district_code': None,
            'gender': None,
            'birth_year': None,
            'age': None
        }
    else:
        # Parse the ID card number components
        id_info['province_code'] = x[:2]
        id_info['city_code'] = x[:4]
        id_info['district_code'] = x[:6]

        if int(x[6:8]) > 31:
            id_info['gender'] = 'FEMALE'
        else:
            id_info['gender'] = 'MALE'

        if int(x[-6]) == 0 or int(x[-6]) == 1:
            id_info['birth_year'] = int('20' + x[-6:-4])
        else:
            id_info['birth_year'] = int('19' + x[-6:-4])

        # Calculate the age using the birth year and the current year
        current_year = datetime.now().year
        id_info['age'] = current_year - id_info['birth_year']

        # Get the province name using the province code
        id_info['province_name'] = province_list.get(id_info['province_code'])

        # Get the province group using the province code
        id_info['province_group'] = get_province_group(id_info['province_code'])

    return id_info


if __name__ == '__main__':
    while True:
        id_card_number = input("Enter an Indonesian ID card number (16 digits): ")
        if len(id_card_number) != 16:
            print("Invalid input. Please enter a 16-digit ID card number.")
            continue
        parsed_id_card = get_id_info(id_card_number)
        if None in parsed_id_card.values():
            print("Invalid ID card number. Please enter a valid 16-digit ID card number.")
            continue
        # Use f-strings to print the parsed ID card components
        print(f"Province: {parsed_id_card['province_name']}, Province Group: {parsed_id_card['province_group']}, City Code: {parsed_id_card['city_code']}, District Code: {parsed_id_card['district_code']}, Gender: {parsed_id_card['gender']}, Birth Year: {parsed_id_card['birth_year']}, Age: {parsed_id_card['age']}")
        print(parsed_id_card)
        break
