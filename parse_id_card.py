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


def parse_id_card(x: str):
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

    If the input is not 16 characters long, returns a list of None values.
    """
    # implementation of the function
    
    if len(x) != 16:
        return [None, None, None, None, None, None]

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

    province_name = province_list.get(id_province)

    return [province_name, id_city, id_district, id_gender, id_birthyear]

if __name__ == '__main__':
    id_card_number = input("Enter an Indonesian ID card number: ")
    parsed_id_card = parse_id_card(id_card_number)
    print(parsed_id_card)