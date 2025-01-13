#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route('/print/<string:username>')
def print_string(username):
    print(username)
    return username


@app.route('/count/<int:number>')

def count(number):
    numbers= "\n".join (str(num) for num in range(number)) + "\n"
    return f'{numbers}'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math_operations(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div" and num2 != 0:
        result = num1 / num2
    elif operation == "%" and num2 != 0:
        result = num1 % num2
    else:
        return "Invalid operation or division by zero.", 400  # HTTP 400 Bad Request
    
    return str(result)  # Convert result to a string for the HTTP response




if __name__ == '__main__':
    app.run(port=5555, debug=True)
