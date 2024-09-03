import sqlite3
from faker import Faker
import random

# Ініціалізуємо Faker
fake = Faker()

# Створюємо підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Заповнюємо таблицю груп
groups = ['Group A', 'Group B', 'Group C']
cursor.executemany('INSERT INTO groups (name) VALUES (?)', [(group,) for group in groups])

# Заповнюємо таблицю викладачів
teachers = [(fake.name(),) for _ in range(4)]
cursor.executemany('INSERT INTO teachers (name) VALUES (?)', teachers)

# Заповнюємо таблицю предметів
subjects = [('Mathematics', 1), ('Physics', 2), ('Chemistry', 3), ('Biology', 4), ('History', 1), ('English', 2)]
cursor.executemany('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', subjects)

# Заповнюємо таблицю студентів
students = [(fake.name(), random.choice([1, 2, 3])) for _ in range(30)]
cursor.executemany('INSERT INTO students (name, group_id) VALUES (?, ?)', students)

# Заповнюємо таблицю оцінок
grades = []
for student_id in range(1, 31):
    for subject_id in range(1, 7):
        for _ in range(random.randint(10, 20)):
            grade = random.randint(1, 12)
            date_of = fake.date_this_year()
            grades.append((student_id, subject_id, grade, date_of))

cursor.executemany('INSERT INTO grades (student_id, subject_id, grade, date_of) VALUES (?, ?, ?, ?)', grades)

# Зберігаємо зміни та закриваємо з'єднання
conn.commit()
conn.close()
