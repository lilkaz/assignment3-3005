import os
from sqlalchemy import create_engine, Column, Integer, String, Date, text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date


#connecting to database

user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@localhost/school_db")



# OR manually type in here your postgre username and password to establish connection to database
# user = "myuser"
# password = "mypassword"

# engine = create_engine(f"postgresql+psycopg2://{user}:{password}@localhost/school_db")



#Check if the connection if successful
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print("connected to postgre")
except Exception as e:
    print("connection failed", e)

Base = declarative_base()







#Student base class
class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    enrollment_date = Column(Date)


# Drop the table if it exists
# Student.__table__.drop(engine, checkfirst=True)


#Create a table if doesn't exist
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


#CRUD operations

#get all students
def getAllStudents():
    print("List of students")
    students = session.query(Student).order_by(Student.student_id).all()
    for s in students:
        print(s.student_id, s.first_name, s.last_name, s.email, s.enrollment_date)


#add student -> check if there is already a student the email
def addStudent(first_name, last_name, email, enrollment_date):
    existing = session.query(Student).filter_by(email=email).first()
    if existing:
        print(f"Students with {existing.email} email already exists, skipping")
        return

    new_student = Student(first_name=first_name, last_name=last_name, email=email, enrollment_date=enrollment_date)
    session.add(new_student)
    session.commit()


#update email if student already exists
def updateStudentEmail(student_id, new_email):
    student = session.query(Student).filter_by(student_id=student_id).first()
    if student:
        student.email = new_email
        session.commit()

#delete if exists
def deleteStudent(student_id):
    student = session.query(Student).filter_by(student_id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        

if __name__ == "__main__":

    addStudent("Alex", "James", "1@example.com", "2025-09-01")
    updateStudentEmail(3, "updated@gmail.com")
    deleteStudent(1)
    getAllStudents()

    
