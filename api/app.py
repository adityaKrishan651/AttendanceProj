import time
from flask import Flask, jsonify, request
from csv_methods import *

app = Flask(__name__)


@app.route('/healthcheck')
def healthcheck():
  return jsonify({'Status': 'Working'})

@app.route('/api/students/<string:name>')
def students(name):
    all_students = view_students(f'files/{ name }.csv')

    return jsonify({'students': all_students})

@app.route('/api/classes')
def classes():
    all_classes = view_classes('files/class_list.csv')
    return jsonify({'classes': all_classes})

@app.route('/api/class/<string:name>')
def view_class(name):
    file_name = f"files/{name}.csv"
    class_details = class_list(file_name)

    return class_details


@app.route('/api/add_student', methods=['POST'])
def add_student():
    data = request.get_json()

    details = {'Roll Number': data['roll_number'], 'class_name': data['class_name']}
    add_students(details)

    return 'Done', 201

@app.route('/api/add_class', methods=['POST'])
def add_class():
    data = request.get_json()

    details = {'name': data['name']}
    add_new_class(details, 'files/class_list.csv')

    return "Done", 201

@app.route('/api/mark_absentees', methods=['POST'])
def mark_absentees():
    data = request.get_json()

    absentees = list(data['absentees'])
    date = data['date']
    class_name = data['class_name']
    write_attendance(absentees, date, class_name)

    return jsonify({'Message': 'Database Successfully Updated'})


