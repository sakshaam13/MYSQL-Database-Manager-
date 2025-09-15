# Student Information Management System  

## 📌 Overview  
This is a **menu-driven Python application** that connects with a **MySQL database** to manage student information. The project allows users to **Display, Add, and Update** student records stored in the `s_info` table of the `student` database.  

It demonstrates how Python can be integrated with MySQL to perform **basic CRUD operations** effectively.  

---

## ⚙️ Features  
- **Display Data** → View all student records in a clean tabular format.  
- **Add Data** → Insert new student details (Name, Class, Roll No., Marks).  
- **Update Data** → Modify existing records using Roll Number as the key.  
- **Auto Table Creation** → Creates the `s_info` table if it doesn’t already exist.  
- **Error Handling** → Handles invalid menu choices and allows safe program exit.  

---

## 🛠️ Requirements  
- Python 3.x  
- MySQL Server  
- Python Library:  
  ```bash
  pip install mysql-connector-python
````

---

## 🚀 How to Run

1. Clone or download the project.
2. Ensure MySQL is installed and running.
3. Create a database named `student` in MySQL:

   ```sql
   CREATE DATABASE student;
   ```
4. Run the Python script:

   ```bash
   python Student_Info_Manager.py
   ```
5. Choose an option from the menu:

   * **1 → Display Database**
   * **2 → Add Data**
   * **3 → Update Data**

---

## 📂 Table Schema

```sql
CREATE TABLE IF NOT EXISTS s_info (
    name VARCHAR(20) NOT NULL,
    class INT NOT NULL,
    rollno INT PRIMARY KEY,
    marks INT NOT NULL
);
```

---

## 👨‍💻 Author

Prepared by **Saksham Rao Chaturvedi**
