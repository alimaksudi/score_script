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

# This dictionary contains the scores for whether the customer has a phone or not.
has_phone_scores = {
    'yes': 6,
    'no': 8
}

# This dictionary contains the scores for different marital statuses.
marital_status_scores = {
    'married': -2,
    'single': 7,
    'divorced': 4,
    'unknown': -5 
}

# This dictionary contains the scores for whether the customer has NPWP or not.
has_npwp_scores = {
    'yes': 6,
    'no': 2
}

# This dictionary contains the scores for different income to debt ratios.
income_todebt_ratio_scores = {
    (0, 4.0): -4,
    (4.0, 5.0): 1,
    (5.0, 6.0): 6,
    (6.0, 100.0): 14
}

# This dictionary contains the scores for different products.
producter_new_scores = {
    'p1': 7,
    'p2': 3,
    'p3': 2,
    'p4': 0,
    'p5': -4
}

# This dictionary contains the scores for different education levels.
education_scores = {
    'e1': 2,
    'e2': -1,
    'e3': -8
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
    'group1': 2,
    'group2': -1,
    'group3': -5
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
    'It6months': -4,
    '6m to 2year': -3,
    '2 years to 5 years': 2,
    '5years+': 4
}

# This dictionary contains the scores for different phone types.
phone_type_scores = {
    'home&office': 4,
    'office': -2,
    'home': -2,
    'none': -3
}

def calculate_final_score(gender, age, has_phone, marital_status, has_npwp, income_todebt_ratio, producter_new, education, work_year, province, num_dependents, home_ownership, length_stay, phone_type):
    """
    Calculates the final score for a customer based on their gender, age, phone, marital status, and NPWP.

    Parameters:
    gender (str): The gender of the customer.
    age (int): The age of the customer.
    has_phone (str): Whether the customer has a phone or not.
    marital_status (str): The marital status of the customer.
    has_npwp (str): Whether the customer has NPWP or not.
    income_todebt_ratio (float): The income to debt ratio of the customer.
    producter_new (str): The product of the customer.
    education (str): The education level of the customer.
    work_year (float): The work year of the customer.
    province (str): The province of the customer.
    num_dependents (int): The number of dependents of the customer.
    home_ownership (str): The home ownership status of the customer.
    length_stay (str): The length of stay of the customer.
    phone_type (str): The type of phone of the customer.

    Returns:
    float: The final score for the customer.
    """
    # Calculate age score
    age_score = None
    for age_range, score in age_scores.items():
        if age_range[0] <= age <= age_range[1]:
            age_score = score
            break
    if age_score is None:
        raise ValueError(f'Invalid age: {age}')

    # Calculate gender score
    gender_score = gender_scores.get(gender.lower(), None)
    if gender_score is None:
        raise ValueError(f'Invalid gender_scores: {gender}')

    # Calculate has_phone score
    has_phone_score = has_phone_scores.get(has_phone.lower(), None)
    if has_phone_score is None:
        raise ValueError(f'Invalid has_phone_scores: {has_phone}')

    # Calculate marital_status score
    marital_status_score = marital_status_scores.get(marital_status.lower(), None)
    if marital_status_score is None:
        raise ValueError(f'Invalid marital_status_scores: {marital_status}')

    # Calculate has_npwp score
    has_npwp_score = has_npwp_scores.get(has_npwp.lower(), None)
    if has_npwp_score is None:
        raise ValueError(f'Invalid has_npwp_scores: {has_npwp}')

    # Calculate income_todebt_ratio score
    income_todebt_ratio_score = None
    for income_range, score in income_todebt_ratio_scores.items():
        if income_range[0] <= income_todebt_ratio <= income_range[1]:
            income_todebt_ratio_score = score
            break
    if income_todebt_ratio_score is None:
        raise ValueError(f'Invalid income_todebt_ratio: {income_todebt_ratio}')

    # Calculate producter_new score
    producter_new_score = producter_new_scores.get(producter_new.lower(), None)
    if producter_new_score is None:
        raise ValueError(f'Invalid producter_new_score: {producter_new}')

    # Calculate education score
    education_score = education_scores.get(education.lower(), None)
    if education_score is None:
        raise ValueError(f'Invalid education_score: {education}')

    # Calculate work_year score
    work_year_score = None
    for work_year_range, score in work_year_scores.items():
        if work_year_range[0] <= work_year <= work_year_range[1]:
            work_year_score = score
            break
    if work_year_score is None:
        raise ValueError(f'Invalid work_year: {work_year}')

    # Calculate province score
    province_score = province_scores.get(province.lower(), None)
    if province_score is None:
        raise ValueError(f'Invalid province_score: {province}')

    # Calculate num_dependents score
    num_dependents_score = None
    for num_dependents_range, score in num_dependents_scores.items():
        if num_dependents_range[0] <= num_dependents <= num_dependents_range[1]:
            num_dependents_score = score
            break
    if num_dependents_score is None:
        raise ValueError(f'Invalid num_dependents: {num_dependents}')

    # Calculate home_ownership score
    home_ownership_score = home_ownership_scores.get(home_ownership.lower(), None)
    if home_ownership_score is None:
        raise ValueError(f'Invalid home_ownership_score: {home_ownership}')

    # Calculate length_stay score
    length_stay_score = length_stay_scores.get(length_stay.lower(), None)
    if length_stay_score is None:
        raise ValueError(f'Invalid length_stay_score: {length_stay}')

    # Calculate phone_type score
    phone_type_score = phone_type_scores.get(phone_type.lower(), None)
    if phone_type_score is None:
        raise ValueError(f'Invalid phone_type_score: {phone_type}')

    # Calculate total score
    base_score = 621
    total_score = sum([
        base_score, age_score, gender_score, has_phone_score, marital_status_score,
        has_npwp_score, income_todebt_ratio_score, producter_new_score, education_score,
        work_year_score, province_score, num_dependents_score, home_ownership_score,
        length_stay_score, phone_type_score
    ])

    return total_score

