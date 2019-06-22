import stu_api


class Student(object):
    def __init__(self, stu_id):
        self.id = stu_id

    # 1.交作业（提交作业时需要先选择班级在选择具体上课节数）[ 0.1 打印学员可以提交作业的上课记录(status == "NO") ]
    def setStatus(self):
        records = stu_api.getStuAtten(self.id)
        print("%10s\t%10s\t%20s" % ("attend_id", "score", "status"))
        for record in records:
            print("%10s\t%10s\t%20s" % (record.attend_id, record.score, record.status))
        if len(records) > 0:
            attend_id = input("输入要交作业的attend_id>>:")
            stu_api.setStatus(self.id, attend_id)
        else:
            print("无未交作业")
    # 2.查看作业成绩
    def checkScore(self):
        self.getMyGrades()
        grade_id = input("输入你的班级id>>:").strip()
        self.getMyRecord(grade_id)
        # attend_id = input("输入要查询成绩的attend_id>>:")
        # records = stu_api.getScore(self.id, attend_id)
        # print("%10s\t%10s\t%20s" % ("attend_id", "score", "status"))
        # for record in records:
        #     print("%10s\t%10s\t%20s" % (record.attend_id, record.score, record.status))
    # 3.查看自己的班级成绩排名
    def checkRank(self):
        self.getMyGrades()
        grade_id = input("输入班级id>>:").strip()
        self.getMyRecord(grade_id)
        attend_id = input("输入attend_id>>:").strip()
        print("你的班级排名：%s" % stu_api.getranking(self.id, attend_id))


    # 5.查看自己班级
    def getMyGrades(self):
        grades = stu_api.getMyClass(self.id)
        print("班级情况")
        print("%5s\t%20s" % ("id", "content"))
        for grade in grades:
            print("%5s\t%20s"% (grade.id, grade.content))

    # 6.查看班级课程记录
    def getMyRecord(self, grade_id):
        stu_attends = stu_api.getStuRecord(self.id, grade_id)
        print("%10s\t%10s\t%10s\t" % ("attend_id", "score", "status"))
        for stu_attend in stu_attends:
            print("%10s\t%10s\t%10s\t" % (stu_attend.attend_id, stu_attend.score, stu_attend.status))


if __name__ == '__main__':
    pass
    # stu = Student()
    # # stu.setStatus()
    # stu.checkRank()