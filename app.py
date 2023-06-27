from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@mysql:3306/students?host=mysql'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()

    student_list = []
    for student in students:
        student_data = {
            'id': student.id,
            'name': student.name,
            'age': student.age
        }
        student_list.append(student_data)

    return jsonify(student_list)



@app.route('/')
def hello():
    return 'Hello, Flask with MySQL on Docker!'

@app.route('/test')
def test():
    new_student = Student(name='John Doe', age=20)
    db.session.add(new_student)
    db.session.commit()
    return 'new student created'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(host='0.0.0.0', debug=True)
