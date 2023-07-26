def parse_id_card(x: str):
    """
    Parses an Indonesian ID card number and returns a list of its components.

    Args:
    x (str): The ID card number to be parsed. Must be 16 characters long.

    Returns:
    list: A list containing the following components of the ID card number:
        - The province code (2 characters)
        - The city code (4 characters)
        - The district code (6 characters)
        - The gender ('MALE' or 'FEMALE')
        - The birth year (4 digits)

    If the input is not 16 characters long, returns a list of None values.
    """
    # implementation of the function
    
    if len(x) != 16:
        return [None, None, None, None, None]

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

    return [id_province, id_city, id_district, id_gender, id_birthyear]

a = parse_id_card('5202082711880001')
print(a)