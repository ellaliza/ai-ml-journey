# 🗃 SQL Snippets

This document serves as a quick reference for commonly used SQL queries in my projects.

---

## 🏗 1. Create Database & Tables

```sql
CREATE DATABASE IF NOT EXISTS student_performance;

USE student_performance;

CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    math INT,
    science INT,
    english INT
);

CREATE TABLE IF NOT EXISTS payments (
    student_id INT,
    amount DECIMAL(6,2),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
```

---

## 📝 2. Insert Records

```sql
INSERT INTO students VALUES (1, 85, 78, 90);
INSERT INTO payments VALUES (1, 500.00);
```

---

## 🔍 3. Select & Where

```sql
SELECT * FROM students;
SELECT math FROM students WHERE student_id = 1;
SELECT * FROM students WHERE math > 80;
```

---

## 📊 4. Aggregation

```sql
SELECT AVG(math) AS avg_math, AVG(science) AS avg_science FROM students;
SELECT MAX(math) FROM students;
SELECT MIN(science) FROM students;
SELECT COUNT(*) FROM payments;
```

---

## 🔗 5. Joins

```sql
-- Inner Join
SELECT s.student_id, s.math, p.amount
FROM students s
JOIN payments p ON s.student_id = p.student_id;

-- Left Join
SELECT s.student_id, s.math, p.amount
FROM students s
LEFT JOIN payments p ON s.student_id = p.student_id;
```

---

## 🧮 6. Order By & Limit

```sql
SELECT * FROM payments ORDER BY amount DESC LIMIT 5;
```

---

## 🛠 7. Alter Table

```sql
ALTER TABLE payments MODIFY amount DECIMAL(6, 2);
ALTER TABLE students ADD gender VARCHAR(10);
```

---

## 🔄 8. Update & Delete

```sql
UPDATE students SET math = 95 WHERE student_id = 1;
DELETE FROM payments WHERE student_id = 10;
```

---

## 🧠 9. Subqueries & Grouping

```sql
-- Student with highest math score
SELECT student_id, math FROM students
WHERE math = (SELECT MAX(math) FROM students);

-- Grouped summary
SELECT student_id, COUNT(*) FROM payments GROUP BY student_id;
```

---

📌 _This file will grow as I learn more about SQL._
