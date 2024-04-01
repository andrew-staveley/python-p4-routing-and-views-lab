#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = range(parameter)
    strig = ''
    for number in numbers:
        strig_old = strig
        strig_new = f'{strig_old}' + f'{number}\n'
        strig = strig_new
    return strig

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    answer = 0
    number_one = int(num1)
    number_two = int(num2)
    if operation == "+":
        answer = number_one + number_two
    elif operation == "-":
        answer = number_one - number_two
    elif operation == "*":
        answer = number_one * number_two
    elif operation == "div":
        answer = number_one / number_two
    elif operation == "%":
        answer = number_one % number_two
    return f'{answer}'
if __name__ == '__main__':
    app.run(port=5555, debug=True)
