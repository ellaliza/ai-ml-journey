# 🎓 Student Performance Project

This project analyzes and visualizes student academic performance and payment records using **Python**, **MySQL**, and **Matplotlib**. It simulates a dataset of 100 students, stores it in a MySQL database, and provides insights using statistical queries and visualizations.

---

## 📊 Features

- ✅ Automatically generates random data for:
  - Math, Science, and English scores
  - Tuition payment records
- ✅ Stores all records in a MySQL database with foreign key constraints
- ✅ Calculates subject-wise average scores
- ✅ Identifies students with the highest and lowest scores
- ✅ Visualizes data using:
  - Bar charts (average scores)
  - Histograms (score distribution)
  - Scatter plots (score correlation)
  - Pie charts (top payments)

---

## 🛠 Technologies Used

- **Python 3**
- **NumPy** – Data generation and manipulation
- **Matplotlib** – Visualization
- **MySQL** – Data storage
- **mysql-connector-python** – Database connectivity

---

## 🚀 How It Works

1. Connects to a local MySQL database.
2. Creates a `student_performance` database (if it doesn’t exist).
3. Creates and populates `students` and `payments` tables.
4. Executes SQL queries to extract insights.
5. Uses `matplotlib` to generate:
   - Average score bar chart
   - Grouped histogram of scores
   - Scatter plot (Math vs Science)
   - Pie chart of top 12 payments

---

## 📂 File Structure
student_performance_project/
│
├── student_performance.py # Main Python script
├── README.md # Project overview and documentation

---

## 🧠 What I Learned

- How to use MySQL with Python using `mysql.connector`
- Creating and managing SQL tables with foreign keys
- Writing and executing SQL queries from Python
- Generating and visualizing data using NumPy and Matplotlib
- Applying database concepts to a real-world-like scenario

---

## 📈 Sample Visualizations

*You can include sample screenshots or generated plots here once you have them.*

---

## 💡 Future Improvements

- Add user input or CSV-based data insertion
- Expand database schema (e.g., add gender, class level)
- Build a web dashboard using Flask or Django
- Add performance trends over time

---

## 📚 About Me

I’m [Your Name], a Computer Engineering student passionate about AI, data science, and backend development. This project is part of my journey into machine learning and data-driven applications.

---

## 🌐 Connect With Me

- GitHub: [ellaliza](https://github.com/ellaliza)
- LinkedIn: [your-linkedin-profile](https://linkedin.com/in/your-profile)