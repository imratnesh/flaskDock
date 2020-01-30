# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import prediction as p

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def ratings():
    text = request.form.get('text')
    if text is None:
        result = ''
    else:
        prediction = p.Prediction.predict(text).upper()
        result = 'Rating is ' + str(prediction)
    return render_template("index.html", name="Ratnesh",
                           pred=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
