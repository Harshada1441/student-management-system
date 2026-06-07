from flask import Flask, render_template, request, redirect, session, send_file

from reportlab.pdfgen import canvas

from flask_mail import Mail, Message

from ml_model import predict_student

import os

from werkzeug.utils import secure_filename

from database import (
    create_table,
    add_student,
    get_all_students,
    count_students,
    delete_student,
    get_student_by_id,
    update_student,
    search_students,
    mark_attendance,
    update_marks,
    get_student_marks,
    create_default_users,
    login_user,
    get_average_marks,
    get_top_student,
    get_recent_students,
    get_student_by_name,
    register_user,
    save_document,
    get_documents,
    get_top_5_students,
get_low_performers,
get_average_attendance,
get_ranked_students,
get_subject_averages
)

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = "student_management_secret_key"


# Create Database Table
create_table()
create_default_users()

def teacher_required():

    if "username" not in session:
        return False

    if session["role"] != "teacher":
        return False

    return True


# login route / Home Route
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = login_user(
            username,
            password
        )

        print(user)

        if user:

            session["username"] = user[1]
            session["role"] = user[3]

            if user[3] == "teacher":
                return redirect("/dashboard")

            else:
                return redirect("/student-dashboard")

        return "Invalid Login"

    return render_template("login.html")



# register 
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]

        register_user(
            username,
            password,
            role
        )

        # Student role असेल तर students table मध्ये add कर
        if role == "student":

            add_student(
                username,      # name
                18,            # default age
                "Not Assigned" # default course
            )

        return redirect("/")

    return render_template(
        "register.html"
    )



# student dashboard
@app.route("/student-dashboard")
def student_dashboard():

    if "username" not in session:
        return redirect("/")

    student = get_student_by_name(
        session["username"]
    )

    if not student:
        return "Student Profile Not Found"

    marks = student[5]

    if marks >= 240:
        performance = "Excellent Student"

    elif marks >= 150:
        performance = "Good Student"

    else:
        performance = "Needs Improvement"

    return render_template(
        "student_dashboard.html",
        student=student,
        performance=performance
    )

@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect("/")

    if session["role"] != "teacher":
        return redirect("/")

    total_students = count_students()

    avg_marks = get_average_marks()

    top_student = get_top_student()

    recent_students = get_recent_students()

    top_students = get_top_5_students()

    low_students = get_low_performers()

    avg_attendance = get_average_attendance()

    subject_avg = get_subject_averages()
    print("SUBJECT AVG = ",subject_avg)


    return render_template(
    "dashboard.html",

    total_students=total_students,
    avg_marks=avg_marks,
    top_student=top_student,
    recent_students=recent_students,

    top_students=top_students,
    low_students=low_students,
    avg_attendance=avg_attendance,

    subject_avg=subject_avg
)

# add logout 
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# Add Student
@app.route("/add-student", methods=["GET", "POST"])
def add_student_page():

    if not teacher_required():
        return redirect("/")

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        add_student(name, age, course)

        return redirect("/students")

    return render_template("add_student.html")


# View Students
@app.route("/students")
def students():

    if not teacher_required():
        return redirect("/")

    student_list = get_all_students()

    return render_template(
        "students.html",
        students=student_list
    )


# Search Students
@app.route("/search")
def search():

    keyword = request.args.get("keyword")

    student_list = search_students(keyword)

    return render_template(
        "students.html",
        students=student_list
    )


# Attendance
@app.route("/attendance/<int:id>")
def attendance(id):

    mark_attendance(id)

    return redirect("/students")


# Delete Student
@app.route("/delete-student/<int:id>")
def delete_student_route(id):

    delete_student(id)

    return redirect("/students")


# Edit Student
@app.route("/edit-student/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    student = get_student_by_id(id)

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        update_student(
            id,
            name,
            age,
            course
        )

        return redirect("/students")

    return render_template(
        "edit_student.html",
        student=student
    )

# marks
@app.route("/marks/<int:id>", methods=["GET", "POST"])
def marks(id):

    student = get_student_by_id(id)

    if request.method == "POST":

        math = request.form["math"]
        science = request.form["science"]
        english = request.form["english"]

        update_marks(
            id,
            math,
            science,
            english
        )

        return redirect("/students")

    return render_template(
        "marks.html",
        student=student
    )




# AI route
@app.route("/prediction/<int:id>")
def prediction(id):

    if not teacher_required():
        return redirect("/")

    student = get_student_by_id(id)

    result = predict_student(

        student[6],   # math
        student[7],   # science
        student[8],
        student[4]   # english

    )

    return render_template(
        "prediction.html",
        marks=student[5],
        result=result
    )




# pdf route
@app.route("/report/<int:id>")
def report(id):

    student = get_student_by_id(id)

    pdf_name = f"student_{id}_report.pdf"

    c = canvas.Canvas(pdf_name)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(200, 800, "Student Report")

    c.setFont("Helvetica", 12)

    c.drawString(100, 740, f"Name: {student[1]}")
    c.drawString(100, 710, f"Age: {student[2]}")
    c.drawString(100, 680, f"Course: {student[3]}")
    c.drawString(100, 650, f"Attendance: {student[4]}")
    c.drawString(100, 620, f"Marks: {student[5]}")

    if student[5] >= 240:
        result = "Excellent Student"

    elif student[5] >= 150:
        result = "Good Student"

    else:
        result = "Needs Improvement"

    c.drawString(100, 590, f"Performance: {result}")

    c.save()

    return send_file(
        pdf_name,
        as_attachment=True
    )



#upload 
@app.route("/upload/<int:id>", methods=["GET", "POST"])
def upload_file(id):

    if request.method == "POST":

        file = request.files["document"]

        if file:

            filename = secure_filename(
                file.filename
            )

            file.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    filename
                )
            )
            
            save_document(
                id,
                filename
            )

            return "File Uploaded Successfully"

    return render_template(
        "upload.html",
        student_id=id
    )



# student wise files route
@app.route("/files/<int:id>")
def student_files(id):

    documents = get_documents(id)

    return render_template(
        "files.html",
        documents=documents
    )



# files route
@app.route("/files")
def files():

    import os

    file_list = os.listdir("uploads")

    return render_template(
        "files.html",
        files=file_list
    )



#download route
@app.route("/download/<filename>")
def download_file(filename):

    return send_file(
        f"uploads/{filename}",
        as_attachment=True
    )




# Run App
if __name__ == "__main__":
    app.run(debug=True)



