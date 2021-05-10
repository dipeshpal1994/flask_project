from flask import Flask, jsonify

app = Flask(__name__)
courses = [{'name': 'x',
            'course_id': '0',
            'description': 'xyz',
            'price': '0'},
           {'name': 'a',
            'course_id': '1',
            'description': 'abc',
            'price': '1'},
           {'name': 'b',
            'course_id': '2',
            'description': 'bcd',
            'price': '2'},
           {'name': 'c',
            'course_id': '3',
            'description': 'cde',
            'price': '3'},
           {'name': 'd',
            'course_id': '4',
            'description': 'def',
            'price': '4'}]


@app.route('/')
def index():
    return 'Welcome Dipesh to Flask world'


@app.route('/courses', methods=['GET'])
def get():
    return jsonify({'Courses': courses})


@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    return jsonify({'Courses': courses[course_id]})


@app.route('/courses/', methods=['POST'])
def create():
    course = {'name': 'e',
              'course_id': '5',
              'description': 'efg',
              'price': '5'}
    courses.append(course)
    return jsonify({'Created': course})
    # curl -i -H 'Content-Type: Application/json' -X POST http://localhost:5000/courses/


@app.route('/courses/<int:course_id>', methods=['PUT'])
def course_update(course_id):
    courses[course_id]['description'] = 'JKL'
    return jsonify({'course': courses[course_id]})
    # curl -i -H 'Content-Type: Application/json' -X PUT http://localhost:5000/courses/5


@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result': True})
    # curl -i -H 'Content-Type: Application/json' -X DELETE http://localhost:5000/courses/5


if __name__ == '__main__':
    app.run(debug=True)
