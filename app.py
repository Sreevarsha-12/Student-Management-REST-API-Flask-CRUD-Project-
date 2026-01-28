from flask import Flask, request, jsonify

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return "API Running"

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify({"message": "Student added", "student": data})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
