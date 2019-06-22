import teacher_api


class Teacher(object):
    def __init__(self, teacher_id):
        self.teacher_id = teacher_id

    # 1.创建班级
    def createGrade(self):
        grade_name = input("输入班级名称>>:").strip()
        teacher_api.createGrade(self.teacher_id, grade_name)
    # 2.通过学员qq号将学员加入学生-班级
    def joinStu(self):
        qq = input("输入学员qq>>:").strip()
        self.getGrade()
        grade_id = input("输入要加入的班级id>>:").strip()
        teacher_api.joinGrade(qq, grade_id)
    # 3.创建班级上课记录（同时为班上的每一位学员创建一条上课记录）
    def createRecord(self):
        self.getGrade()
        grade_id = input("输入班级id>>:").strip()
        content = input("记录描述>>:").strip()
        teacher_api.createGradeAttendRecord(grade_id, content)
    # 4.为班级学员打分
    def score(self):
        self.getStu()
        stu_id = input("输入学员id>>:").strip()
        attend_id = input("输入attend_id>>:").strip()
        score = input("输入分数>>:").strip()
        teacher_api.score(stu_id, attend_id, score)

    # 5.获取班级的成员及上课记录
    def getStu(self):
        self.getGrade()
        grade_id = input("输入班级id>>:").strip()
        students = teacher_api.getStu(grade_id)
        print("%10s\t%15s\t%15s" % ("stu_id", "qq", "name"))
        for student in students:
            print("%10s\t%15s\t%15s" % (student.id, student.qq, student.name))
        records = teacher_api.getClassRecord(grade_id)
        print("%10s\t%30s" % ("attend_id", "content"))
        for record in records:
            print("%10s\t%30s" % (record.id, record.content))

    # 6.获取老师的班级
    def getGrade(self):
        grades = teacher_api.getClass(self.teacher_id)
        print("%5s\t%30s" % ("id", "content"))
        for grade in grades:
            print("%5s\t%30s" % (grade.id, grade.content))

if __name__ == '__main__':
    pass
    # teacher = Teacher(1)
    # teacher.getGrade()
    # teacher = Teacher()
    # teacher.score()

