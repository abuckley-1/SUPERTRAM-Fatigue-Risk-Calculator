from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>SUPERTRAM Fatigue Risk Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }
        .container {
            max-width: 700px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
            color: #0078D4;
        }
        form {
            display: grid;
            gap: 12px;
        }
        input[type=number], input[type=submit] {
            padding: 10px;
            font-size: 16px;
            width: 100%;
        }
        input[type=submit] {
            background-color: #0078D4;
            color: white;
            border: none;
            cursor: pointer;
        }
        input[type=submit]:hover {
            background-color: #005fa3;
        }
        .logo {
            text-align: center;
            margin-bottom: 20px;
        }
        .logo img {
            max-width: 180px;
        }
        .readme-link {
            text-align: center;
            margin-top: 30px;
        }
        .readme-link a {
            background-color: #0078D4;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
        }
        .readme-link a:hover {
            background-color: #005fa3;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <img src="https://raw.githubusercontent.com/abuckley-1-Fatigue-Risk-Calculator/main/SupertramLogo.jpg
        </div>
        <h2>SUPERTRAM Fatigue Risk Calculator</h2>
        <form method="post">
            Duty Length (minutes): <input type="number" name="duty_length" required>
            Rest Length (minutes): <input type="number" name="rest_length" required>
            Commuting Time (minutes): <input type="number" name="commute" required>
            Job Workload (1-3): <input type="number" name="workload" min="1" max="3" required>
            Job Attention (1-3): <input type="number" name="attention" min="1" max="3" required>
            Break Frequency (minutes): <input type="number" name="break_freq" required>
            Break Average Length (minutes): <input type="number" name="break_avg" required>
            Continuous Work Length (minutes): <input type="number" name="cont_work" required>
            Break After Continuous Work (minutes): <input type="number" name="break_after_cont" required>
            <input type="submit" value="Calculate Fatigue Index">
        </form>
        {% if fatigue_index is not none %}
            <h3 style="text-align:center; margin-top:20px;">Calculated Fatigue Index: {{ fatigue_index }}</h3>
        {% endif %}
        <div class="readme-link">
            <a href="https://github.com/abuckley-1-Fatigue-Risk-Calculator/blob/main/README.md</div>
    </div>
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
        except ValueError as e:
            print("Error:", e)
            fatigue_index = "Invalid input. Please enter numeric values."

    return render_template_string(HTML_TEMPLATE, fatigue_index=fatigue_index)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
