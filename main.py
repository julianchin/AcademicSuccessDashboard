from flask import Flask, render_template, url_for
app = Flask(__name__)

advisees = [
    {
        'name': 'Mary Smith',
        'department': 'Computer Science',
        'degree_level': 'Senior',
        'email': 'msmith5@illinois.edu',
        'wireless_status':'danger',
        'compass_status':'warning',
        'moodle_status':'success'
    },
    {
        'name': 'John Doe',
        'department': 'Information Sciences',
        'degree_level': 'PhD',
        'email': 'jdoe2@illinois',
        'wireless_status':'success',
        'compass_status':'warning',
        'moodle_status':'success'
    }
]


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/advisor")
def advisor():
    return render_template('advisor.html', advisees=advisees)


if __name__ == '__main__':
    app.run(debug=True)