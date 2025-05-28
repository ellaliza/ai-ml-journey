import numpy as np
from matplotlib import pyplot as plt
import mysql.connector

dbms = mysql.connector.connect(
    host="localhost",
    user="user", 
    password = "password")

cursor = dbms.cursor()

# store in database
cursor.execute('CREATE DATABASE IF NOT EXISTS student_performance;')
cursor.execute('USE student_performance;')
cursor.execute('CREATE TABLE IF NOT EXISTS students (student_id INT PRIMARY KEY NOT NULL, math INT, science INT, english INT);')
cursor.execute('CREATE TABLE IF NOT EXISTS payments (student_id INT, amount DECIMAL(3, 2), FOREIGN KEY (student_id) REFERENCES student_performance.students(student_id));')
cursor.execute('ALTER TABLE payments modify amount decimal(6, 2);')
# insert data into the database

cursor.execute('select count(student_id) from students;')
count = cursor.fetchall()
print(f'Total number of students: {count[0][0]} \n \n')

if not(count[0][0] > 0):
    # create 100 students
    student_ids = np.arange(1, 101)

    # create math, english and science scores
    math_scores, english_scores, science_scores = (np.random.randint(30, 100, 300)).reshape(3, 100)

    # create payment records
    list_of_payments = [np.random.randint(10, 100) * 100 for i in range(100)]
    payments = np.array(list_of_payments)

    for id, math_score, science_score, english_score in zip(student_ids, math_scores, science_scores, english_scores):
        cursor.execute(f'INSERT INTO students VALUES ({id}, {math_score}, {science_score}, {english_score});')

    for id, payment in zip(student_ids, payments):
        cursor.execute(f'INSERT INTO payments VALUES ({id}, {payment});')

    dbms.commit()

cursor.execute('''select 
               avg(math) as 'Math Average', 
               avg(science) as 'Science Average', 
               avg(english) as 'English Average' from students;''')

averages = cursor.fetchall()
for (math_avg, science_avg, english_avg) in averages:
    print(f'Math Average: {math_avg}')
    print(f'Science Average: {science_avg}')
    print(f'English Average: {english_avg} \n\n')

cursor.execute('select student_id, math from students where math = (select max(math) from students);')
max_math = cursor.fetchall()
students_with_highest_math_score = [str(row[0]) for row in max_math]
max_math_students = ', '.join(students_with_highest_math_score)
print(f'Student(s) with highest math score have IDs {max_math_students} with a score of {max_math[0][1]} \n\n')

cursor.execute('select student_id, math from students where math = (select min(math) from students);')
min_math = cursor.fetchall()
students_with_lowest_math_score = [str(row[0]) for row in min_math]
min_math_students = ', '.join(students_with_lowest_math_score)
print(f'Student(s) with lowest math score have IDs {min_math_students} with a score of {min_math[0][1]} \n\n')

### Data Visualization ###
# Create a figure for visualizations
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(ncols = 2, nrows=2, figsize=(12, 12))

# Create a bar chart for the average scores
def create_bar_chart(averages, axes):
    subjects = ['Math', 'Science', 'English']
    avg_scores = [averages[0][0], averages[0][1], averages[0][2]]

    axes.bar(subjects, avg_scores, color=['#5281ce','#bae8ac', '#ff7582'], width=0.9)
    axes.set_xlabel('Subjects')
    axes.set_ylabel('Average Scores')
    axes.set_title('Average Scores of Students')

# fetch math scores
subjects = ['math', 'science', 'english']
scores = {}
for i in subjects:
    cursor.execute(f'select {i} from students;')
    scores[i] = [row[0] for row in cursor.fetchall()]

def create_histogram(scores, axes):
    ranges = np.arange(30, 110, 10)
    axes.hist([scores['math'], scores['science'], scores['english']], 
             bins=ranges, 
             label=['Math', 'Science', 'English'], 
             edgecolor='black', 
             alpha=0.7, 
             color=['#5281ce','#bae8ac', '#ff7582'] )
    
    # Add labels and title
    axes.set_xlabel("Score Ranges")
    axes.set_ylabel("Number of Students")
    axes.set_title("Grouped Histogram of Student Scores")
    axes.legend(title="subjects")

cursor.execute('select student_id, amount from payments order by amount desc limit 12;')
payments = cursor.fetchall()
ids = np.array([str(row[0]) for row in payments])
print(ids)
amounts = np.array([row[1] for row in payments])
def create_piechart(payments, ids, axes):
    axes.pie(payments, labels = ids, colors = ['#487EB0', '#53E0BC', '#F0DF87', '#8395A7','#5281ce','#bae8ac', '#ff7582'], autopct='%1.2f%%', pctdistance=0.9, labeldistance=.6, textprops={'fontsize': 8})
    axes.set_title('Top 12 Payments', loc='left', y=1.0, pad=-8)

def create_scatter(scores, axes):
    axes.scatter(scores['math'], scores['science'], color='#ff7582', label='Math vs Science')
    axes.set_xlabel('Math Scores')
    axes.set_ylabel('Science Scores')
    axes.set_title('Scatter Plot of Math vs Science Scores')

    

create_scatter(scores, ax4)
create_piechart(amounts, ids, ax3)
create_histogram(scores, ax2)
create_bar_chart(averages, ax1)
# Display the histogram
plt.show()