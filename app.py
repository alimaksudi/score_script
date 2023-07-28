from flask import Flask, request, render_template
from score import calculate_final_score

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id_card_number = request.form['id_card_number']
        has_phone = request.form['has_phone']
        marital_status = request.form['marital_status']
        education = request.form['education']
        work_year = float(request.form['work_year'])
        province = request.form['province']
        num_dependents = int(request.form['num_dependents'])
        home_ownership = request.form['home_ownership']
        length_stay = request.form['length_stay']
        phone_type = request.form['phone_type']

        final_score = calculate_final_score(id_card_number, has_phone, marital_status, education, work_year, province, num_dependents, home_ownership, length_stay, phone_type)
        return render_template('result.html', final_score=final_score)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)