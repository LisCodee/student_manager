import Teacher
import Student
import stu_api
import teacher_api


def createStudent():
        qq = input("输入qq号>>:").strip()
        name = input("输入姓名>>:").strip()
        id = stu_api.createStu(qq, name)
        print("\033[31m请牢记你的id:%s\033[0m" % id)

def createTeacher():
    name = input("输入名字>>:").strip()
    entry_date = input("输入入职日期>>:").strip()
    id = teacher_api.createTeacher(name, entry_date)
    print("\033[31m请牢记你的id:%s\033[0m" % id)

def teacherMenu(teacher:Teacher):
    while True:
        print("--------------1.创建班级--------------")
        print("--------------2.加入学生--------------")
        print("--------------3.创建记录--------------")
        print("--------------4.批改作业--------------")
        print("--------------5.获取记录--------------")
        print("--------------6.获取班级--------------")
        print("--------------0.退出登录--------------")
        choose = input("请选择>>:").strip()
        if choose == "1":
            teacher.createGrade()
        elif choose == "2":
            teacher.joinStu()
        elif choose == '3':
            teacher.createRecord()
        elif choose == "4":
            teacher.score()
        elif choose == '5':
            teacher.getStu()
        elif choose == '6':
            teacher.getGrade()
        elif choose == '0':
            main()
            break


def studentMenu(student:Student):
    while True:
        print("--------------1.提交作业--------------")
        print("--------------2.查看成绩--------------")
        print("--------------3.查看排名--------------")
        print("--------------4.查看班级--------------")
        print("--------------0.退出登录--------------")
        choose = input("请选择>>:").strip()
        if choose == "1":
            student.setStatus()
        elif choose == "2":
            student.checkScore()
        elif choose == "3":
            student.checkRank()
        elif choose == "4":
            student.getMyGrades()
        elif choose == "0":
            main()
            break


def showModel(num):
    print("--------------1.login--------------")
    print("--------------2.register--------------")
    print("--------------3.exit---------------")
    choose = input("choose>>:").strip()
    if num == 2:            # 老师
        if choose == "1":
            teacher_id = int(input("input your teacher id>>:").strip())
            teacher = Teacher.Teacher(teacher_id)
            teacherMenu(teacher)
        elif choose == "2":
            createTeacher()
            main()
        elif choose == "3":
            exit(0)
        else:
            print("\033[31mInput Error!\033[0m")
    elif num == 1:          # 学生
        if choose == "1":
            stu_id = input("input your student id>>:").strip()
            student = Student.Student(stu_id)
            studentMenu(student)
        elif choose == "2":
            createStudent()
            main()
        elif choose == "3":
            exit(0)
        else:
            print("\033[31mInput Error!\033[0m")
    else:
        main()


def main():
    print("--------------1.student------------")
    print("--------------2.teacher------------")
    choose = input("choose>>:").strip()
    if choose == "1":
        showModel(1)
    elif choose == "2":
        showModel(2)
    else:
        print("\033[31mInput error\033[0m")


if __name__ == '__main__':
    main()
