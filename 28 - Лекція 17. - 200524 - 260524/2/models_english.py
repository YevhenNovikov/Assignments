from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    subjects = relationship('Subject', secondary='student_subjects', back_populates='students')

class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    students = relationship('Student', secondary='student_subjects', back_populates='subjects')

class StudentSubject(Base):
    __tablename__ = 'student_subjects'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'), primary_key=True)


DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'


engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='postgres',
        user='postgres',
        password='****',
        port=5432,
    )
)



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_student1 = Student(name="John Doe")
new_student2 = Student(name="Jane Smith")
new_subject1 = Subject(name="English")
new_subject2 = Subject(name="Mathematics")

session.add(new_student1)
session.add(new_student2)
session.add(new_subject1)
session.add(new_subject2)
session.commit()

student_subject1 = StudentSubject(student_id=new_student1.id, subject_id=new_subject1.id)
student_subject2 = StudentSubject(student_id=new_student2.id, subject_id=new_subject1.id)

session.add(student_subject1)
session.add(student_subject2)
session.commit()

english_subject = session.query(Subject).filter(Subject.name == 'English').one()
students = session.query(Student).join(StudentSubject).filter(StudentSubject.subject_id == english_subject.id).all()

for student in students:
    print(student.name)