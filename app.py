from flask import Flask, redirect, render_template, request
from request_jobs import run_app
import csv
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/write_csv1', methods=['POST'])
def write_csv1():
    if request.method == 'POST':
        keyword = "keyword"
        location = "location"
        variables = [
            request.form.get('variable1'),
            request.form.get('variable2'),
            request.form.get('variable3'),
            request.form.get('variable4')
        ]

        if not variables:
            return render_template('index.html', error='Missing variables.')

        filename = 'search_terms.csv'
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([keyword, location])  # Write the keyword and location
            for variable in variables:
                if variable:
                    writer.writerow(variable.split(','))  # Write each variable line

        return render_template('result.html', filename=filename)
    
    return render_template('index.html')

@app.route('/write_csv2', methods=['POST'])
def write_csv2():
    if request.method == 'POST':
        name = "name"
        email = "email"
        variables = [
            request.form.get('variable1'),
            request.form.get('variable2'),
            request.form.get('variable3'),
            request.form.get('variable4')
        ]

        if not variables:
            return render_template('index.html', error='Missing variables.')

        filename = 'contacts.csv'
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email])  # Write the keyword and location
            for variable in variables:
                if variable:
                    writer.writerow(variable.split(','))  # Write each variable line

        return render_template('result.html', filename=filename)

    return render_template('index.html', filename=filename)

@app.route('/start_program', methods=['POST'])
def start_program():
    run_app()

    return render_template('result.html', message='Python program started successfully.')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
