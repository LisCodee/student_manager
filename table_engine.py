from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, ForeignKey, String, Column, create_engine, DATE, Table

Base = declarative_base()


# 讲师类
class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    entry_date = Column(DATE, nullable=False)

    def __repr__(self):
        return self


# 学员类
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, autoincrement=True, primary_key=True)
    qq = Column(String(20), nullable=False)
    name = Column(String(30), nullable=False)

    def __repr__(self):
        return self


# 班级类
class Grade(Base):
    __tablename__ = "grade"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(256), nullable=False)

    def __repr__(self):
        return self


# 讲师-班级
class Teacher_grade(Base):
    __tablename__ = 'teacher_grade'
    id = Column(Integer, autoincrement=True, primary_key=True)
    teacher_id = Column(Integer, ForeignKey("teacher.id"))
    grade_id = Column(Integer, ForeignKey("grade.id"))

    def __repr__(self):
        return self


# 学员-班级
class Stu_grade(Base):
    __tablename__ = 'stu_grade'
    id = Column(Integer, autoincrement=True, primary_key=True)
    stu_id = Column(Integer, ForeignKey('student.id'))
    grade_id = Column(Integer, ForeignKey('grade.id'))

    def __repr__(self):
        return self


# 上课记录
class Grade_attend(Base):
    __tablename__ = "grade_attend"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(255), nullable=False)

    def __repr__(self):
        return self


# 班级上课记录
class Class_attend(Base):
    __tablename__ = 'class_attend'
    id = Column(Integer, autoincrement=True, primary_key=True)
    grade_id = Column(Integer, ForeignKey('grade.id'))
    attend_id = Column(Integer, ForeignKey('grade_attend.id'))

    def __repr__(self):
        return self


# 学员-上课记录
class Stu_attend(Base):
    __tablename__ = 'stu_attend'
    id = Column(Integer, autoincrement=True, primary_key=True)
    stu_id = Column(Integer, ForeignKey('student.id'))
    attend_id = Column(Integer, ForeignKey('grade_attend.id'))
    score = Column(Integer)
    status = Column(String(30), nullable=False)

    def __repr__(self):
        return self


engine = create_engine("mysql+pymysql://root:123456@localhost/student_manager?charset=utf8", encoding="utf-8", echo=False)
# Base.metadata.create_all(engine)