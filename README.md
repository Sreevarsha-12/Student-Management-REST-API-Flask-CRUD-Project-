## 📚 Student Management REST API (Flask CRUD Project)

This project is a simple **Student Management REST API** built using **Python Flask**. It demonstrates basic **CRUD operations (Create, Read, Update, Delete)** using HTTP methods and JSON data. The API is tested using **Postman**.

---

## 🚀 Features

* Add new student records (POST)
* Get all students (GET)
* Get student by ID (GET)
* Update student details (PUT)
* Delete student by ID (DELETE)
* JSON-based request and response handling

---

## 🛠️ Technologies Used

* Python 3
* Flask (Web Framework)
* Postman (API Testing)

---

## 📁 Project Structure

```
student-api/
│
├── app.py        # Main Flask application
├── README.md     # Project documentation
└── requirements.txt (optional)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/student-api.git
cd student-api
```

### 2️⃣ Install Dependencies

```bash
pip install flask
```

### 3️⃣ Run the Application

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000/
```

---

## 🔗 API Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | `/`              | Home route        |
| POST   | `/students`      | Add a student     |
| GET    | `/students`      | Get all students  |
| GET    | `/students/<id>` | Get student by ID |
| PUT    | `/students/<id>` | Update student    |
| DELETE | `/students/<id>` | Delete student    |

---

## 📥 Sample JSON Request

### Add Student (POST `/students`)

```json
{
  "id": 1,
  "name": "Sreevarsha",
  "course": "CSE",
  "marks": 90
}
```

---

## 🧪 Testing with Postman

1. Open Postman
2. Choose HTTP Method (POST/GET/PUT/DELETE)
3. Enter URL (example):

   ```
   http://127.0.0.1:5000/students
   ```
4. For POST/PUT, go to **Body → raw → JSON** and paste JSON data
5. Click **Send**

---

## ⚠️ Notes

* This project uses **in-memory storage**, so data will be lost when the server restarts.
* For real-world applications, integrate a database like **SQLite, MySQL, or MongoDB**.

---

## 👨‍💻 Author

**Sreevarsha Tadakamalla**

---

## 📜 License

This project is for educational purposes and free to use.
