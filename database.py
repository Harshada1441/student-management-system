import sqlite3


def create_connection():
    conn = sqlite3.connect("database/students.db")
    return conn



def create_table():

    conn = create_connection()

    cursor = conn.cursor()

    # Students Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT,
        attendance INTEGER DEFAULT 0,
        marks INTEGER DEFAULT 0,
        math INTEGER DEFAULT 0,
        science INTEGER DEFAULT 0,
        english INTEGER DEFAULT 0
    )
    """)

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        filename TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_student(name, age, course):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    conn.close()


def get_all_students():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return students


def count_students():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def delete_student(student_id):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()


def get_student_by_id(student_id):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    return student


def update_student(student_id, name, age, course):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE students
        SET name=?, age=?, course=?
        WHERE id=?
        """,
        (name, age, course, student_id)
    )

    conn.commit()
    conn.close()


def search_students(keyword):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM students
        WHERE name LIKE ?
        """,
        ('%' + keyword + '%',)
    )

    students = cursor.fetchall()

    conn.close()

    return students


def mark_attendance(student_id):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE students
        SET attendance = attendance + 1
        WHERE id = ?
        """,
        (student_id,)
    )

    conn.commit()
    conn.close()


def update_marks(student_id, math, science, english):

    total = int(math) + int(science) + int(english)

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE students
        SET math=?,
            science=?,
            english=?,
            marks=?
        WHERE id=?
        """,
        (
            math,
            science,
            english,
            total,
            student_id
        )
    )

    conn.commit()
    conn.close()


# student marks
def get_student_marks(student_id):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT marks
        FROM students
        WHERE id=?
        """,
        (student_id,)
    )

    result = cursor.fetchone()

    conn.close()

    return result[0]



# add user function
def create_default_users():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO users
        (username,password,role)
        VALUES
        ('admin','admin123','teacher')
        """
    )

    cursor.execute(
        """
        INSERT OR IGNORE INTO users
        (username,password,role)
        VALUES
        ('student','student123','student')
        """
    )

    conn.commit()
    conn.close()


def login_user(username,password):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=?
        AND password=?
        """,
        (username,password)
    )

    user = cursor.fetchone()

    conn.close()

    return user




# avg marks 
def get_average_marks():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT AVG(marks) FROM students"
    )

    result = cursor.fetchone()[0]

    conn.close()

    if result is None:
        return 0

    return round(result, 2)



# student top
def get_top_student():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, marks
        FROM students
        ORDER BY marks DESC
        LIMIT 1
        """
    )

    student = cursor.fetchone()

    conn.close()

    return student


# recent student
def get_recent_students():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, course
        FROM students
        ORDER BY id DESC
        LIMIT 5
        """
    )

    students = cursor.fetchall()

    conn.close()

    return students


def get_average_marks():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT AVG(marks) FROM students"
    )

    result = cursor.fetchone()[0]

    conn.close()

    if result is None:
        return 0

    return round(result, 2)


def get_top_student():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, marks
        FROM students
        ORDER BY marks DESC
        LIMIT 1
        """
    )

    student = cursor.fetchone()

    conn.close()

    return student


def get_recent_students():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, course
        FROM students
        ORDER BY id DESC
        LIMIT 5
        """
    )

    students = cursor.fetchall()

    conn.close()

    return students


def get_student_by_name(name):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE name=?
        """,
        (name,)
    )

    student = cursor.fetchone()

    conn.close()

    return student


# register 
def register_user(username, password, role):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users(username,password,role)
        VALUES(?,?,?)
        """,
        (username,password,role)
    )

    conn.commit()
    conn.close()
    
    
# save documents
def save_document(student_id, filename):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO documents(student_id, filename)
        VALUES(?,?)
        """,
        (student_id, filename)
    )

    conn.commit()
    conn.close()
    
# fetch student documents
def get_documents(student_id):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM documents
        WHERE student_id=?
        """,
        (student_id,)
    )

    documents = cursor.fetchall()

    conn.close()

    return documents


def get_top_5_students():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, marks
        FROM students
        ORDER BY marks DESC
        LIMIT 5
        """
    )

    students = cursor.fetchall()

    conn.close()

    return students


def get_low_performers():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, marks
        FROM students
        ORDER BY marks ASC
        LIMIT 5
        """
    )

    students = cursor.fetchall()

    conn.close()

    return students


def get_average_attendance():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT AVG(attendance)
        FROM students
        """
    )

    result = cursor.fetchone()[0]

    conn.close()

    if result is None:
        return 0

    return round(result, 2)


def get_subject_averages():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
        AVG(math),
        AVG(science),
        AVG(english)
        FROM students
        """
    )

    result = cursor.fetchone()

    conn.close()

    return result



def get_ranked_students():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, marks
        FROM students
        ORDER BY marks DESC
        """
    )

    students = cursor.fetchall()

    conn.close()

    return students