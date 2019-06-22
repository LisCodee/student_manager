import table_engine
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=table_engine.engine)
session = Session_class()


# 0.创建学员
def createStu(qq, name):
    stu_obj = table_engine.Student(qq=qq, name=name)
    session.add(stu_obj)
    session.commit()
    stu_id = session.query(table_engine.Student).filter(table_engine.Student.qq == qq).first()
    return stu_id

# 0.0 查看学生上课记录
def getStuRecord(stu_id, grade_id):
    attend_objs = session.query(table_engine.Class_attend).filter(table_engine.Class_attend.grade_id == grade_id).all()
    attend_recs = []
    for attend_obj in attend_objs:
        stu_attend_obj = session.query(table_engine.Stu_attend).filter(table_engine.Stu_attend.stu_id == stu_id)\
            .filter(table_engine.Stu_attend.attend_id == attend_obj.attend_id).first()
        if str(type(stu_attend_obj)) == "<class 'NoneType'>":
            pass
        else:
            attend_recs.append(stu_attend_obj)
    # attend_recs = session.query(table_engine.Stu_attend).filter(table_engine.Stu_attend.stu_id == stu_id).filter(
    #     table_engine.Stu_attend.status == "NO").all()
    return attend_recs

# 0.1 打印学员可以提交作业的上课记录(status == "NO")
def getStuAtten(stu_id):
    attend_recs = session.query(table_engine.Stu_attend).filter(table_engine.Stu_attend.stu_id == stu_id).filter(
                                                               table_engine.Stu_attend.status == "NO").all()
    return attend_recs


# 1.交作业（提交作业时需要先选择班级在选择具体上课节数）
def setStatus(stu_id, attend_id):
    """
    交作业
    :param stu_id: 学生id
    :param attend_id: 学生-上课记录id
    :return:
    """
    stu_record_obj = session.query(table_engine.Stu_attend).filter(table_engine.Stu_attend.stu_id == stu_id).filter(
                                                                   table_engine.Stu_attend.attend_id == attend_id).first()
    stu_record_obj.status = "YES"
    session.commit()


# 2.查看作业成绩
def getScore(stu_id, attend_id):
    stu_record = session.query(table_engine.Stu_attend).filter(table_engine.Stu_attend.stu_id == stu_id).filter(
                                                               table_engine.Stu_attend.attend_id == attend_id).first()
    grade_attend = session.query(table_engine.Grade_attend).filter(table_engine.Grade_attend.id == attend_id).first()
    return grade_attend.content, stu_record.score       # 返回课程记录描述以及分数


# 3.查看自己的班级成绩排名
def getranking(stu_id, grade_id):
    stu_records = session.query(table_engine.Stu_attend).filter(table_engine.Stu_attend.attend_id ==
                                                                grade_id).order_by(table_engine.Stu_attend.score.desc()).all()
    score = 1
    for stu_record in stu_records:
        if stu_id == stu_record.stu_id:
            return score
        score += 1

    return -1       # 没有对应匹配项


# 4.查看自己的课程
# def getClass(stu_id):
#     stu_grades = session.query(table_engine.Stu_grade).filter(table_engine.Stu_grade.stu_id == stu_id).all()
#     grades = []
#     for stu_grade in stu_grades:
#         grades.append(session.query(table_engine.Grade).filter(table_engine.Grade.id == stu_grade.id).first())
#     return grades       # 返回课程对象列表


# 5.根据qq号获取stu_id
def getStuid(qq):
    stu_obj = session.query(table_engine.Student).filter(table_engine.Student.qq == qq).first()
    return stu_obj.id


# 6.查看自己班级
def getMyClass(stu_id):
    stu_grades = session.query(table_engine.Stu_grade).filter(table_engine.Stu_grade.stu_id == stu_id).all()
    grades = []
    for stu_grade in stu_grades:
        grades.append(session.query(table_engine.Grade).filter(table_engine.Grade.id == stu_grade.grade_id).first())
    return grades

if __name__ == '__main__':
    pass
    # grades = getStuRecord(1, 1)
    # for grade in grades:
    #     print(grade.score)
    # createStu('2646485096', 'zgh')
    # recods = getStuAtten(1)
    # for recod in recods:
    #     print(recod.attend_id)
    # setStatus(1, 2)
    # content, score = getScore(1, 2)
    # print(content, score)
    # getranking(2, 3)
    # print("")
    # grades = getMyClass(1)
    # for grade in grades:
    #     print(grade.content)
    # print(getStuid("1376417539"))