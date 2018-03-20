from flask import Flask, render_template, request

from src.mbta_helper import find_stop_near

app = Flask(__name__) #*****

app.config['DEBUG'] = True

app.secret_key = "Some secret string here" #*****

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/calc/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        location = request.form['a']
        stop, distance = find_stop_near(location)

        if stop:
            return render_template('calculator_result.html',
                                   s=stop, d=distance)
        else:
            return render_template('calculator_form.html', error=True)
    return render_template('calculator_form.html', error=None)


if __name__ == '__main__':
    app.run()
