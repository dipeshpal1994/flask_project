from flask import Flask, jsonify

app = Flask(__name__)

employee = [{'name': 'a',
             'id': '1',
             'password': 'a'},
            {'name': 'b',
             'id': '2',
             'password': 'b'}]


@app.route('/', methods=['GET'])
def courses():
    return "Welcome Dipu to Flask"


@app.route('/emp/', methods=['GET'])
def get_emp():
    return jsonify({'employee': employee})


@app.route('/emp/<int:index>', methods=['GET'])
def get_employee(index):
    return jsonify(employee[index])


@app.route('/emp/', methods=['POST'])
def post_emp():
    emp = {'name': 'c',
           'id': '3',
           'password': 'c'}
    employee.append(emp)
    return jsonify({'employee': emp})


@app.route('/emp/<int:index>', methods=['PUT'])
def put_emp(index):
    employee[index]['password'] = 'z'
    return jsonify({'employee': employee[index]})


@app.route('/emp/<int:index>', methods=['DELETE'])
def delete(index):
    employee.remove(employee[index])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug=True)
