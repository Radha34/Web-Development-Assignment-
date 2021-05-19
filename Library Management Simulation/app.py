import os
from flask import Flask, render_template, request,send_file,redirect,url_for,make_response
from flask.globals import session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination
import datetime
from datetime import  timedelta  
from werkzeug.utils import secure_filename
import pandas as pd

UPLOAD_FOLDER='static/que_ppr/'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:radha@localhost:5432/library"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)



#---------models-----------#
class Students(db.Model):
    __tablename__ = 'students'
 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique= True)
    password = db.Column(db.String(20))
    repassword = db.Column(db.String(20))
    
 
    def __init__(self, name,email,password,repassword):
        self.name = name
        self.email = email
        self.password = password
        self.repassword = repassword

class Teachers(db.Model):
    __tablename__ = 'teachers'
 
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique= True)
    password = db.Column(db.String(20))
    repassword = db.Column(db.String(20))
 
    def __init__(self, name,email,password,repassword):
        self.name = name
        self.email = email
        self.password = password
        self.repassword = repassword

class Guests(db.Model):
    __tablename__ = 'guests'
    name = db.Column(db.String)
    email = db.Column(db.String, primary_key = True)

    def __init__(self,email,name):
        
        self.email = email
        self.name = name

class Books(db.Model):
    __tablename__ = 'books'
    isbn = db.Column(db.String,primary_key = True,)
    title = db.Column(db.String) 
    author = db.Column(db.String)
    category = db.Column(db.String)
    count = db.Column(db.Integer)
    form_type = db.Column(db.String)


    def __init__(self,isbn,title,author,category,count,form_type):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.category = category
        self.count = count
        self.form_type = form_type

class Issued_Books(db.Model):
    __tablename__ = 'issued_books'
    transID=db.Column(db.Integer, primary_key=True)
    BookIsbn = db.Column(db.String, nullable=False)
    userID=db.Column(db.Integer,nullable=False)    
    IssueDate = db.Column(db.Date, nullable=False)
    ExpRetDate = db.Column(db.Date,nullable=False)
    ActRetDate = db.Column(db.Date)
    fine = db.Column(db.Integer)
    BookTilte = db.Column(db.String,nullable=False)
    
class Question_Ppr(db.Model):
    
    __tablename__ = 'question_ppr'
    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.String)
    exam = db.Column(db.String)
    year = db.Column(db.Integer)
    file = db.Column(db.String)

    def __init__(self,subject,exam,year,file):
        self.subject = subject
        self.exam = exam
        self.year = year
        self.file = file

class Issued_Books_teacher(db.Model):
    __tablename__ = 'issued_books_teachers'
    transID=db.Column(db.Integer, primary_key=True)
    BookIsbn = db.Column(db.String, nullable=False)
    userID=db.Column(db.Integer,nullable=False)    
    IssueDate = db.Column(db.Date, nullable=False)
    ExpRetDate = db.Column(db.Date,nullable=False)
    ActRetDate = db.Column(db.Date)
    fine = db.Column(db.Integer)
    BookTilte = db.Column(db.String,nullable=False)

#----------routes-----------# 



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def index_():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
      if request.method =='POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['pass']
        repassword = request.form['re_pass']
        category = request.form['category']
        if password != repassword or len(password) < 8:
            return render_template('register.html',message="Passwords doesnt match")
        if category == 'Student':    
            if db.session.query(Students).filter(Students.email == email).count()==0:
                new_user = Students(name, email,password,repassword)
                db.session.add(new_user)
                db.session.commit()
                return render_template('index.html')  
        else :
            if db.session.query(Teachers).filter(Teachers.email==email).count()==0:    
                new_teacher = Teachers(name,email,password,repassword)
                db.session.add(new_teacher)
                db.session.commit()
                return render_template('index.html')
        return render_template ('register.html',message="Already exist.")

@app.route('/register')
def register():
    return render_template("register.html")
       
#--------ADMIN ROUTES---------#    
@app.route('/deletebook/<string:bookisbn>/')
def dltbook(bookisbn):
    book_isbn = bookisbn
    print(book_isbn)
    books = db.session.query(Books).all()
    students = db.session.query(Students).all()
    student_count = db.session.query(Students).count()
    book_count = db.session.query(Books).count()
    que_ppr = db.session.query(Question_Ppr).all()
    teachers = db.session.query(Teachers).all()
    guests = db.session.query(Guests).all()
    guests_count = db.session.query(Guests).count()
    teachers_count = db.session.query(Teachers).count()
    issued_books_count = db.session.query(Issued_Books).count()+db.session.query(Issued_Books_teacher).count()
    que_ppr_count = db.session.query(Question_Ppr).count()
    issuedbook = db.session.query(Issued_Books).all()
    issuedbookteacher = db.session.query(Issued_Books_teacher).all()
    for book in books:
        if book.isbn == book_isbn:
            db.session.delete(book)
            db.session.commit()            
            books = db.session.query(Books).all()
            for ib in issuedbook:
                if ib.BookIsbn == book_isbn:
                    db.session.delete(ib)
                    db.session.commit()
            for ibt in issuedbookteacher:   
                if ibt.BookIsbn == book_isbn:
                    db.session.delete(ibt)
                    db.session.commit()       
            return render_template('admin_panel.html',que_ppr_count=que_ppr_count,teachers_count=teachers_count,issued_books_count=issued_books_count,guests_count=guests_count,teachers= teachers, books = books,book_count = book_count,students= students,student_count = student_count,que_ppr=que_ppr,guests=guests)     
        
    return render_template('admin_panel.html',que_ppr_count=que_ppr_count,teachers_count=teachers_count,issued_books_count=issued_books_count,guests_count=guests_count,teachers= teachers, books = books,book_count = book_count,students= students,student_count = student_count,que_ppr=que_ppr,guests=guests)     



@app.route('/admin/<int:s_id>/')
def deletestudent(s_id):
    student_id = s_id
    student = Students.query.filter_by(id=student_id).first()
    if student:
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))

@app.route('/admin/<int:t_id>')
def deleteteacher(t_id):
    teacher_id = t_id
    teacher = db.session.query(Teachers).filter_by(id=teacher_id)
    if teacher:
        db.session.delete(teacher)
        db.session.commit()             
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))

@app.route('/admin/<int:q_id>')
def deleteque_ppr(q_id):
    queppr_id = q_id
    queppr = Question_Ppr.query.filter_by(id=queppr_id).first()
    if queppr:
        db.session.delete(queppr)
        db.session.commit()
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))

@app.route('/admin',methods=['GET','POST'])
def admin():
    books = db.session.query(Books).all()
    students = db.session.query(Students).all()
    student_count = db.session.query(Students).count()
    book_count = db.session.query(Books).count()
    que_ppr = db.session.query(Question_Ppr).all()
    teachers = db.session.query(Teachers).all()
    guests = db.session.query(Guests).all()
    guests_count = db.session.query(Guests).count()
    teachers_count = db.session.query(Teachers).count()
    issued_books_count = db.session.query(Issued_Books).count()
    que_ppr_count = db.session.query(Question_Ppr).count()
    
    if request.method == 'POST' and request.form['form_type'] =='bookform':
        form_type=request.form['form_type']
        isbn = request.form['isbn']
        title = request.form['title']
        author = request.form['author']
        category = request.form['category']
        count = request.form['count']
        
        if db.session.query(Books).filter(Books.isbn == isbn).count()==0:
            new_book = Books(isbn, title,author,category,count,form_type)
            db.session.add(new_book)
            db.session.commit()
            
            return render_template('admin_panel.html',que_ppr_count=que_ppr_count,teachers_count=teachers_count,issued_books_count=issued_books_count,guests_count=guests_count,teachers= teachers, books = books,book_count = book_count,students= students,student_count = student_count,que_ppr=que_ppr,guests=guests)  
        else:    
            return render_template ('admin_panel.html',message="Book already exist.",que_ppr_count=que_ppr_count,teachers_count=teachers_count,issued_books_count=issued_books_count,guests_count=guests_count,teachers= teachers, books = books,book_count = book_count,students= students,student_count = student_count,que_ppr = que_ppr,guests=guests)
    
    elif request.method == 'POST' and request.form['form_type'] == 'Login':
        
        if request.form['email'] == 'admin@gmail.com' and request.form['pass'] == 'Password@123':
            return render_template('admin_panel.html',que_ppr_count=que_ppr_count,teachers_count=teachers_count,issued_books_count=issued_books_count,guests_count=guests_count,teachers= teachers, books = books,guests=guests,book_count = book_count,students= students,student_count = student_count,que_ppr = que_ppr)
        else :
            return render_template('index.html',message='Invalid admin credentials') 
    
    elif request.method == 'POST' and request.form['form_type'] == 'Add Question Paper':
        subject = request.form['subject']
        exam = request.form['exam']
        year = request.form['year']
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_queppr = Question_Ppr(subject,exam,year,file.filename)
        db.session.add(new_queppr)
        db.session.commit()      
        que_ppr_count = db.session.query(Question_Ppr).count()
      
        return render_template('admin_panel.html',que_ppr_count=que_ppr_count,teachers_count=teachers_count,issued_books_count=issued_books_count,guests_count=guests_count,teachers= teachers, books = books,book_count = book_count,students= students,student_count = student_count,que_ppr=que_ppr,guests=guests)  
    elif request.method == 'GET':            
        return render_template('index.html',que_ppr_count=que_ppr_count,teachers_count=teachers_count,issued_books_count=issued_books_count,guests_count=guests_count,teachers= teachers, books = books,book_count = book_count,students= students,student_count = student_count,que_ppr=que_ppr,guests=guests)  


#----------TEACHERS ROUTES----------#    

@app.route('/teacher',methods=['GET','POST'])
def teacher():
    user_email = request.form.get('email') 
    password_entered = request.form.get('pass')
    users = db.session.query(Teachers).all()
    books = db.session.query(Books).all()
    issued_books = db.session.query(Issued_Books_teacher).all()
    for user in users:
        if user_email == user.email and password_entered == user.password:
            teacher= user
            return render_template("teachers_panel.html", teacher = teacher,books=books,issued_books=issued_books)
    
    if request.method == 'POST' and request.form['form_type'] == 'Add Question Paper':
        subject = request.form['subject']
        exam = request.form['exam']
        year = request.form['year']
        file = request.files['file']
        data = file.read()
        new_queppr = Question_Ppr(subject,exam,year,data)
        db.session.add(new_queppr)
        db.session.commit()
        que_ppr = db.session.query(Question_Ppr).all()
        books = db.session.query(Books).all()
        return render_template("teachers_panel.html",books=books)
                        
    return render_template("index.html",message="Invalid teacher credentials")   
        

@app.route('/teacherissuedbook/<bookisbn>/<int:t_id>/', methods=['POST','GET'])
def teacherissuedbook(bookisbn,t_id):  
    users = db.session.query(Teachers).all()
    books = db.session.query(Books).all()
    issued_books = db.session.query(Issued_Books_teacher).all()
    que_ppr = db.session.query(Question_Ppr).all()
    book_isbn = bookisbn

    issue_date = datetime.date.today()
    return_date = datetime.date.today()+timedelta(days=15)
    book = db.session.query(Books).filter_by(isbn = book_isbn).update({Books.count:Books.count-1})
        
    bookname = db.session.query(Books).filter_by(isbn = book_isbn).first().title
    if db.session.query(Issued_Books_teacher).filter_by(userID = t_id).count() < 5 :
            new_issued_book = Issued_Books_teacher(BookIsbn = book_isbn,userID=t_id,IssueDate=issue_date,ExpRetDate=return_date,BookTilte=bookname)
            db.session.add(new_issued_book)
            db.session.commit()
            issued_books = db.session.query(Issued_Books_teacher).all()
            for teacher in users:
                if teacher.id == t_id:
                     return render_template('teachers_panel.html',teacher=teacher,books=books,issued_books=issued_books,que_ppr=que_ppr)
    else:
            for teacher in users:
                if teacher.id == t_id:
                     return render_template('student_panel.html',teacher=teacher,books=books,issued_books=issued_books,que_ppr=que_ppr)    

@app.route('/teacher/password/<int:t_id>',methods=['POST','GET']) 
def teacherpass(t_id):
    teach_id = t_id
    teacher = Teachers.query.filter_by(id = teach_id)
    if teacher:
        new_pass = request.form['new_pass']
        re_new_pass = request.form['re_new_pass']
        db.session.query(Teachers).filter_by(id = teach_id).update({Teachers.password:new_pass,Teachers.repassword:re_new_pass}, synchronize_session = False)    
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/teacher/<int:transId>/<int:userID>/',methods=['POST','GET'])
def t_reissuestu(transId,userID):
    trans_ID = transId
    user_id = userID    
    today = datetime.date.today()
    retdate = datetime.date.today()+timedelta(days=15)
    teachers = db.session.query(Teachers).all()
    books = db.session.query(Books).all()
    issued_books = db.session.query(Issued_Books_teacher).all()
    que_ppr = db.session.query(Question_Ppr).all()
    db.session.query(Issued_Books_teacher).filter_by(transID=trans_ID).update({Issued_Books_teacher.IssueDate:today, Issued_Books_teacher.ExpRetDate:retdate},synchronize_session = False)
    db.session.commit()
    for teacher in teachers:
        if student.id == user_id:
            return render_template('teachers_panel.html',teacher = teacher,books=books,issued_books=issued_books,que_ppr=que_ppr)

@app.route('/return/teacher/<int:transID>/<int:userID>/',methods=['GET','POST'])
def t_retissbook(transID,userID):
    trans_ID = transID
    user_id = userID    
    issuedbooks = db.session.query(Issued_Books_teacher).all()
    teachers = db.session.query(Teachers).all()
    books = db.session.query(Books).all()
    que_ppr = db.session.query(Question_Ppr).all()
    for trans in issuedbooks:
        if trans.transID == trans_ID and trans.ExpRetDate >= datetime.date.today():
            for book in books:
                if trans.BookIsbn == book.isbn:
                    book.count = book.count+1
                    db.session.delete(trans)
                    db.session.commit()

        elif trans.transID == trans_ID and trans.ExpRetDate < datetime.date.today():
            days = datetime.date.today() - trans.ExpRetDate
            day_fine = int(days.day)
            db.session.query(Issued_Books_teacher).filter_by(transID=trans_ID).update({Issued_Books_teacher.ActRetDate:datetime.datetime.today(),Issued_Books_teacher.fine: day_fine*2 },synchronize_session = False)
            db.session.commit()
    
    for teacher in teachers:
        if teacher.id == user_id:
            return render_template('teachers_panel.html',teacher = teacher,books = books,que_ppr=que_ppr,issued_books = issuedbooks)  

#-----------STUDENTS ROUTES---------#
@app.route('/student',methods=['GET','POST'])
def student():
    user_email = request.form.get('email') 
    password_entered = request.form.get('pass')
    stu_email = user_email
    stu_pass = password_entered
    users = db.session.query(Students).all()
    books = db.session.query(Books).all()
    issued_books = db.session.query(Issued_Books).all()
    que_ppr = db.session.query(Question_Ppr).all()
    for user in users:
        if stu_email == user.email and stu_pass == user.password:
            student = user
            return render_template("student_panel.html", student = student,books=books,issued_books=issued_books,que_ppr=que_ppr)

    return redirect(url_for('index'))    
    
@app.route('/studentissuedbook/<bookisbn>/<int:stu_id>/', methods=['POST','GET'])
def studentissuedbook(bookisbn,stu_id):      
        users = db.session.query(Students).all()
        books = db.session.query(Books).all()
        issued_books = db.session.query(Issued_Books).all()
        que_ppr = db.session.query(Question_Ppr).all()
        book_isbn = bookisbn

        issue_date = datetime.date.today()
        return_date = datetime.date.today()+timedelta(days=15)
        book = db.session.query(Books).filter_by(isbn = book_isbn).update({Books.count:Books.count-1})
        
        bookname = db.session.query(Books).filter_by(isbn = book_isbn).first().title
        if db.session.query(Issued_Books).filter_by(userID = stu_id).count() < 5 :
            new_issued_book = Issued_Books(BookIsbn = book_isbn,userID=stu_id,IssueDate=issue_date,ExpRetDate=return_date,BookTilte=bookname)
            db.session.add(new_issued_book)
            db.session.commit()
            issued_books = db.session.query(Issued_Books).all()
            for student in users:
                if student.id == stu_id:
                     return render_template('student_panel.html',student=student,books=books,issued_books=issued_books,que_ppr=que_ppr)
        else:
            for student in users:
                if student.id == stu_id:
                     return render_template('student_panel.html',student=student,books=books,issued_books=issued_books,que_ppr=que_ppr)
            
@app.route('/downloadbooklist')
def booklist():
        data = Books.query.all()
        print(data)
        df = pd.DataFrame([(d.isbn, d.title, d.author) for d in data], 
                        columns=['isbn', 'book_name', 'author'])
        df.to_csv('booklist.csv')
        print(df)
        return redirect(url_for('student'))          
          
@app.route('/student/password/<int:s_id>',methods=['POST','GET'])          
def studentpass(s_id):
    stu_id = s_id
    student = Students.query.filter_by(id = stu_id)
    if student:
        new_pass = request.form['new_pass']
        re_new_pass = request.form['re_new_pass']
        db.session.query(Students).filter_by(id = stu_id).update({Students.password:new_pass,Students.repassword:re_new_pass}, synchronize_session = False)    
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/student/<int:transId>/<int:userID>/',methods=['POST','GET'])
def reissuestu(transId,userID):
    trans_ID = transId
    user_id = userID    
    today = datetime.date.today()
    retdate = datetime.date.today()+timedelta(days=15)
    students = db.session.query(Students).all()
    books = db.session.query(Books).all()
    issued_books = db.session.query(Issued_Books).all()
    que_ppr = db.session.query(Question_Ppr).all()
    db.session.query(Issued_Books).filter_by(transID=trans_ID).update({Issued_Books.IssueDate:today, Issued_Books.ExpRetDate:retdate},synchronize_session = False)
    db.session.commit()
    for student in students:
        if student.id == user_id:
            return render_template('student_panel.html',student=student,books=books,issued_books=issued_books,que_ppr=que_ppr)

@app.route('/return/student/<int:transID>/<int:userID>/',methods=['GET','POST'])
def retissbook(transID,userID):
    trans_ID = transID
    user_id = userID    
    issuedbooks = db.session.query(Issued_Books).all()
    students = db.session.query(Students).all()
    books = db.session.query(Books).all()
    que_ppr = db.session.query(Question_Ppr).all()
    for trans in issuedbooks:
        if trans.transID == trans_ID and trans.ExpRetDate >= datetime.date.today():
            for book in books:
                if trans.BookIsbn == book.isbn:
                    book.count = book.count+1
            db.session.delete(trans)
            db.session.commit()

        elif trans.transID == trans_ID and trans.ExpRetDate < datetime.date.today():
            days = datetime.date.today() - trans.ExpRetDate
            day_fine = int(days.day)
            db.session.query(Issued_Books).filter_by(transID=trans_ID).update({Issued_Books.ActRetDate:datetime.datetime.today(),Issued_Books.fine: day_fine*2 },synchronize_session = False)
            db.session.commit()
    
    for student in students:
        if student.id == user_id:
            return render_template('student_panel.html',student=student,books = books,que_ppr=que_ppr,issued_books = issuedbooks)    
    

@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = UPLOAD_FOLDER + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')   
#--------GUEST ROUTES---------#

@app.route('/guest',methods=['POST','GET'])
def guest():
    books = db.session.query(Books).all()
    question_pprs= db.session.query(Question_Ppr).all()
    if request.method =='POST':
        guest_email = request.form['email']
        guest_name = request.form['name']
        
        new_guest = Guests(guest_email,guest_name)
        db.session.add(new_guest)
        db.session.commit()
       
        return render_template('guest_panel.html',books=books, que_ppr= question_pprs)
    return render_template('guest_panel.html',books=books, que_ppr= question_pprs)    

@app.route('/downloadbooklist_guest',methods=['GET','POST'])
def guestbooklist():
    data = Books.query.all()
    print(data)
    df = pd.DataFrame([(d.isbn, d.title, d.author) for d in data], 
                        columns=['isbn', 'book_name', 'author'])
    df.to_csv('guest_booklist.csv')
    
    return redirect(url_for('guest'))






if __name__ == '__main__':
    app.debug=True
    app.run()   