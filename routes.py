from flask import Blueprint, request, jsonify
from database import get_db_connection

student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return jsonify(students)

@student_bp.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    student = cursor.fetchone()
    conn.close()
    if student:
        return jsonify(student)
    return jsonify({'error': 'Student not found'}), 404

@student_bp.route('/students', methods=['POST'])
def create_student():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email, age, major) VALUES (%s, %s, %s, %s)", 
                   (data['name'], data['email'], data['age'], data['major']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Student created successfully'}), 201

@student_bp.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name = %s, email = %s, age = %s, major = %s WHERE id = %s",
                   (data['name'], data['email'], data['age'], data['major'], id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Student updated successfully'})

@student_bp.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Student deleted successfully'})
