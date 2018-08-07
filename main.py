from flask import Flask, render_template, url_for
app = Flask(__name__)

advisors = [
    {
        'name': 'Corey Schafer',
        'Department': 'Computer Science',
        'grade': 'Senior',
        'Email': 'xxx@illinois.edu',
        'Philosophy':'Work hard, play harder!'
    },
    {
        'name': 'John Smith',
        'Department': 'Computer Science',
        'grade': 'PhD',
        'Email': 'xxx@illinois',
        'Philosophy':'Just do it!'
    }
]


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/advisor")
def advisor():
    return render_template('advisor.html', advisors=advisors)


if __name__ == '__main__':
    app.run(debug=True)