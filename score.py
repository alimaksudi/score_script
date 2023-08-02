from parse_id_card import get_id_info

# This dictionary contains the scores for different genders.
gender_scores = {
    'male': -1,
    'female': 1,
    'unknown': 1
}

# This dictionary contains the scores for different age ranges.
age_scores = {
    (0, 30): -5,
    (30, 40): -2,
    (40, 45): 0,
    (45, 1000): 3
}


# This dictionary contains the scores for different marital statuses.
marital_status_scores = {
    'married': -2,
    'single': 7,
    'divorced': 4,
    'unknown': -5
}

# This dictionary contains the scores for different education levels.
education_scores = {
    's2': 2,
    's3':2,
    'specialis': 2,
    's1': -1,
    'sma': -1,
    'smp': -8,
    'other': -8
}

# This dictionary contains the scores for different work years.
work_year_scores = {
    (0, 1.0): -4,
    (1.0, 3.0): -2,
    (3.0, 5.0): 0,
    (5.0, 10.0): 2,
    (10.0, 100.0): 6
}

# This dictionary contains the scores for different provinces.
province_scores = {
    'group_1': 2,
    'group_2': -1,
    'group_3': -5
}

# This dictionary contains the scores for different number of dependents.
num_dependents_scores = {
    (0, 2): 4,
    (2, 4): -2,
    (4, 1000): -9
}

# This dictionary contains the scores for different home ownership statuses.
home_ownership_scores = {
    'selfown': 4,
    'familyown': 2,
    'annirent': -2,
    'mthrent': -3
}

# This dictionary contains the scores for different length of stays.
length_stay_scores = {
    '1t6months': -4,
    '6m to 2year': -3,
    '2 years to 5 years': 2,
    '5years+': 4
}

# This dictionary contains the scores for different phone types.
phone_type_scores = {
    'homeoffice': 4,
    'office': -2,
    'home': -2,
    'none': -3
}
# This dictionary contains the score categories for credit scores, along with their corresponding score ranges.
score_categories = {
    (0, 560): 'Buruk',
    (560, 579): 'Tidak Baik',
    (580, 599): 'Kurang Baik',
    (600, 619): 'Baik',
    (620, 719): 'Sangat Baik',
    (720, 1000): 'Luar Biasa'
}

def calculate_final_score(id_card_number: str, marital_status: str, education: str, work_year: float, num_dependents: int, home_ownership: str, length_stay: str, phone_type: str) -> dict:
    """
    Calculates the final score for a customer based on their gender, age, phone, marital status, and NPWP.

    Parameters:
    id_card_number (str): The ID card number of the customer.
    marital_status (str): The marital status of the customer.
    education (str): The education level of the customer.
    work_year (float): The work year of the customer.
    num_dependents (int): The number of dependents of the customer.
    home_ownership (str): The home ownership status of the customer.
    length_stay (str): The length of stay of the customer.
    phone_type (str): The type of phone of the customer.

    Returns:
    dict: A dictionary containing the final score and score category for the customer.
    """
    # Calculate age score
    parsed_id_card = get_id_info(id_card_number)
    province_group = parsed_id_card['province_group']
    age = parsed_id_card['age']
    gender = parsed_id_card['gender']
    
    age_score = next((score for age_range, score in age_scores.items() if age_range[0] <= age <= age_range[1]), None)
    if age_score is None:
        raise ValueError(f'Invalid age: {age}')

    # Calculate gender score
    gender_score = gender_scores.get(gender.lower())
    if gender_score is None:
        raise ValueError(f'Invalid gender_scores: {gender}')

    # Calculate marital_status score
    marital_status_score = marital_status_scores.get(marital_status.lower())
    if marital_status_score is None:
        raise ValueError(f'Invalid marital_status_scores: {marital_status}')

    # Calculate education score
    education_score = education_scores.get(education.lower())
    if education_score is None:
        raise ValueError(f'Invalid education_score: {education}')

    # Calculate work_year score
    work_year_score = next((score for work_year_range, score in work_year_scores.items() if work_year_range[0] <= work_year <= work_year_range[1]), None)
    if work_year_score is None:
        raise ValueError(f'Invalid work_year: {work_year}')

    # Calculate province score
    province_score = province_scores.get(province_group.lower())
    if province_score is None:
        raise ValueError(f'Invalid province_score: {province_group}')

    # Calculate num_dependents score
    num_dependents_score = next((score for num_dependents_range, score in num_dependents_scores.items() if num_dependents_range[0] <= num_dependents <= num_dependents_range[1]), None)
    if num_dependents_score is None:
        raise ValueError(f'Invalid num_dependents: {num_dependents}')

    # Calculate home_ownership score
    home_ownership_score = home_ownership_scores.get(home_ownership.lower())
    if home_ownership_score is None:
        raise ValueError(f'Invalid home_ownership_score: {home_ownership}')

    # Calculate length_stay score
    length_stay_score = length_stay_scores.get(length_stay.lower())
    if length_stay_score is None:
        raise ValueError(f'Invalid length_stay_score: {length_stay}')

    # Calculate phone_type score
    phone_type_score = phone_type_scores.get(phone_type.lower())
    if phone_type_score is None:
        raise ValueError(f'Invalid phone_type_score: {phone_type}')
    
    # Calculate total score
    base_score = 621
    total_score = sum([
        age_score, gender_score, marital_status_score, education_score,
        work_year_score, province_score, num_dependents_score, home_ownership_score,
        length_stay_score, phone_type_score
    ])
    
    final_score = base_score + total_score
    
    # Define the score categories
    score_category = next((score_categorie for score_range, score_categorie in score_categories.items() if score_range[0] <= final_score <= score_range[1]), None)

    return {'final_score': final_score, 'score_category': score_category}

final_score = calculate_final_score('3204112001000001', 'married', 'sma', 1.0, 0, 'selfown', '1t6months', 'homeoffice')    
print(final_score)
