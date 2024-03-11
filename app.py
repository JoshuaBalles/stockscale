from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history')
def history():
    return render_template('history.html', title='History')

@app.route('/results')
def results():
    return render_template('results.html', title='Results')

if __name__ == '__main__':
    app.run(debug=True)
