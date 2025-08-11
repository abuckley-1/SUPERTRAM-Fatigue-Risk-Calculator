from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>SUPERTRAM Fatigue Risk Calculator</title>
</head>
<body>
    <h2>SUPERTRAM Fatigue Risk Calculator</h2>
    <form method="post">
        Duty Length (minutes): <input type="number" name="duty_length"><br>
        Rest Length (minutes): <input type="number" name="rest_length"><br>
        Commuting Time (minutes): <input type="number" name="commute"><br>
        Job Workload (1-3): <input type="number" name="workload" min="1" max="3"><br>
        Job Attention (1-3): <input type="number" name="attention" min="1" max="3"><br>
        Break Frequency (minutes): <input type="number" name="break_freq"><br>
        Break Average Length (minutes): <input type="number" name="break_avg"><br>
        Continuous Work Length (minutes): <input type="number" name="cont_work"><br>
        Break After Continuous Work (minutes): <input type="number" name="break_after_cont"><br>
        <input type="submit" value="Calculate Fatigue Index">
    </form>
    {% if fatigue_index is not none %}
        <h3>Calculated Fatigue Index: {{ fatigue_index }}</h3>
    {% endif %}
</body>
</html>
"""

def calculate_fatigue_index(duty_length, rest_length, commute, workload, attention,
                            break_freq, break_avg, cont_work, break_after_cont):
    fatigue = (
        0.3 * duty_length +
        0.2 * commute +
        0.1 * workload +
        0.1 * attention -
        0.1 * rest_length -
        0.05 * break_freq +
        0.05 * break_avg -
        0.05 * cont_work +
        0.05 * break_after_cont
    )
    return round(fatigue, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    fatigue_index = None
    if request.method == 'POST':
        try:
            duty_length = int(request.form['duty_length'])
            rest_length = int(request.form['rest_length'])
            commute = int(request.form['commute'])
            workload = int(request.form['workload'])
            attention = int(request.form['attention'])
            break_freq = int(request.form['break_freq'])
            break_avg = int(request.form['break_avg'])
            cont_work = int(request.form['cont_work'])
            break_after_cont = int(request.form['break_after_cont'])

            fatigue_index = calculate_fatigue_index(
                duty_length, rest_length, commute, workload, attention,
                break_freq, break_avg, cont_work, break_after_cont
            )
        except ValueError:
            fatigue_index = "Invalid input. Please enter numeric values."

    return render_template_string(HTML_TEMPLATE, fatigue_index=fatigue_index)

if __name__ == '__main__':
    import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)

