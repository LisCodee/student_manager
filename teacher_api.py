import table_engine
from sqlalchemy.orm import sessionmaker


Session_class = sessionmaker(bind=table_engine.engine)
session = Session_class()
# 创建session实例

# 0.创建讲师
def createTeacher(name, entry_date):
    teacher_obj = table_engine.Teacher(name=name, entry_date=entry_date)
    session.add(teacher_obj)
    session.commit()
    teacher_ids = session.query(table_engine.Teacher).filter(table_engine.Teacher.name == name).all()
    teacher_id = teacher_ids[len(teacher_ids) - 1].id
    return teacher_id


# 1.创建班级
def createGrade(teacher_id, grade_name):
    grade_obj = table_engine.Grade(content=grade_name)      # 班级表插入
    session.add(grade_obj)
    session.commit()    # 先插入班级表
    grades = session.query(table_engine.Grade).filter(table_engine.Grade.content == grade_name).all()    # 获取插入的grade数据
    grade_id = grades[len(grades) - 1].id    # 获取插入的grade数据id
    teacher_grade_obj = table_engine.Teacher_grade(teacher_id=teacher_id, grade_id=grade_id)    # 老师-班级表插入
    session.add(teacher_grade_obj)
    session.commit()            # 再插入老师-班级表


# 2.通过学员qq号将学员加入学生-班级
def joinGrade(qq, grade_id):
    stu_obj = session.query(table_engine.Student).filter(table_engine.Student.qq == qq).first()
    stu_id = stu_obj.id     # 通过qq获取学生的id
    stu_grade_obj = table_engine.Stu_grade(stu_id=stu_id, grade_id=grade_id)
    session.add(stu_grade_obj)          # 将记录插入到学生-班级表
    session.commit()


# 3.创建班级上课记录（同时为班上的每一位学员创建一条上课记录）
def createGradeAttendRecord(grade_id, content):
    """
    为班级上的学生都新建一条上课记录
    :param grade_id: 需要添加的班级
    :param content: 记录说明
    :return:
    """
    createAttendRecord(content)     # 新建一个上课记录
    # 找到上课记录的id
    record_obj = session.query(table_engine.Grade_attend).filter(table_engine.Grade_attend.content == content).all()
    record_id = record_obj[len(record_obj) - 1].id       # 找到上课记录的id
    # print(record_id)
    grade_attend_record_obj = table_engine.Class_attend(grade_id=grade_id, attend_id=record_id)
    session.add(grade_attend_record_obj)            # 插入班级-上课记录
    # session.commit()
    # 为班上每一位学员创建一条上课记录
    student_obj = session.query(table_engine.Stu_grade).filter(table_engine.Stu_grade.grade_id == grade_id).all()
    # print(student_obj[0].id)
    status = "NO"  # 学员出勤情况
    for student in student_obj:
        stu_id = student.id
        stu_attend_obj = table_engine.Stu_attend(stu_id=stu_id, attend_id=record_id, status=status)
        session.add(stu_attend_obj)

    session.commit()


# 3.0 创建上课记录
def createAttendRecord(content):
    # content课堂内容
    attend_record = table_engine.Grade_attend(content=content)
    session.add(attend_record)
    session.commit()        # 插入上课记录

# 4.为班级学员打分
def score(stu_id, attend_id, score):
    """
    为班级的学员打分
    :param stu_id: 需要打分的学员id
    :param attend_id: 学生-记录id
    :param score: 打的分值
    :return:
    """
    stu_records = session.query(table_engine.Stu_attend).filter(table_engine.Stu_attend.stu_id == stu_id).filter(
                                                                table_engine.Stu_attend.attend_id == attend_id).first()
    # print(stu_records.id)
    stu_records.score = score       # 打分
    session.commit()        # 事务提交


# 5.获取班级的成员
def getStu(grade_id):
    """
    获取班级的学生id
    :param grade_id:课程id
    :return:
    """
    grade_students = session.query(table_engine.Stu_grade).filter(table_engine.Stu_grade.grade_id == grade_id).all()
    students = []
    for grade_student in grade_students:
        students.append(session.query(table_engine.Student).filter(table_engine.Student.id ==
                                                                   grade_student.stu_id).first())
    return students         # 返回该班级的所有学生（列表）


# 6.获取老师的班级
def getClass(teacher_id):
    teacher_grades = session.query(table_engine.Teacher_grade).filter(table_engine.Teacher_grade.teacher_id == teacher_id).all()
    grades = []
    for teacher_grade in teacher_grades:
        grades.append(session.query(table_engine.Grade).filter(table_engine.Grade.id == teacher_grade.grade_id).first())
    return grades            # 返回该老师带的所有班级对象(是一个列表)

# 7.获取班级上课记录
def getClassRecord(grade_id):
    class_attends = session.query(table_engine.Class_attend).filter(table_engine.Class_attend.grade_id == grade_id).all()
    records = []
    for class_attend in class_attends:
        grade_attends = session.query(table_engine.Grade_attend).filter(table_engine.Grade_attend.id ==
                                                                        class_attend.attend_id).first()
        records.append(grade_attends)
    return records
if __name__ == '__main__':
    # print("hello word")
    print(createTeacher("wangyali", "2019-03-28"))
    # createGrade(1, "python learn")
    # joinGrade('2646485096', 1)
    # createGradeAttendRecord(1, "python从入门到入土")
    # score(1, 3, 100)
    # score(2, 3, 90)
    # grades = getClass(1)
    # for grade in grades:
    #     print(grade.id)
    # stus = getStu(1)
    # for stu in stus:
    #     print(stu.id)