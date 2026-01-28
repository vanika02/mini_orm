# 🧩 BUILDING A CUSTOM ORM IN PYTHON

This project is a **mini ORM engine built from scratch in python**. It simulates how real ORMs like Django ORM / SQLAlchemy works internally.

It allows me to:
- Pretend Python lists are database tables
- Create tables
- Insert data
- Query data
- Update and delete data
- Understand relationships (Student --> Teacher)

---

## 🏫 A MINI ORM FOR SCHOOL MANAGEMENT SYSTEM

This ORM is built around a simple school system with:
- **Students**
- **Techers**
- A Relationship between them

---

### 📁 Project Structure

mini_orm/
│
├── database.py # Fake database (tables + storage)
├── models.py # Table → Class mapping & insert logic
├── query.py # Query engine (filter, get, update, delete)
├── main.py # Run & test the ORM
└── README.md # Documentation

---

## 🔁 Project Flow

database.py → defines tables
models.py → inserts data using ORM
query.py → fetches / filters data
main.py → runs the project

--- 

## ⚙️ How it Works 

### 1️⃣ database.py
Stores fake tables using python lists and simulates auto-increment IDs.

### 2️⃣ models.py
Maps tables to classes (Student, Teacher) and handles inserts.

### 3️⃣ query.py
Acts like a query engine (Similar to SQL SELECT, UPDATE, DELETE).

### 4️⃣ main.py
This is the entry point where data is created and queried.

---

## ▶️ How to Run

```bash
python3 main.py
```

