def Check(studentscore):
    for f in student.itmes():
        if f[1] >= 50:
            print(f[0], f[1])


studentscore = {'Should Imporve':0-49,'Good':50-89,'exally':90-1000,}
Check(Student score)

class School:
    def __init__(self, subject='student score'):
        print('ตรวจเกรด')
        self.subject = subject

class Student(School):
    def __init__(self, fullname, score, subject):
        super().__init__(subject)
        self.fullname = fullname
        self.score = score

    def checkGrade(self):
        if self.score >= 80:
            print(f' ได้เกรด 4')
        elif self.score >= 70:
            print(f' ได้เกรด 3')
        elif self.score >= 60:
            print(f' ได้เกรด 2')
        elif self.score >= 50:
            print(f' ได้เกรด 1')
        else:
            print(f' ได้เกรด 0')

print('===============')
student01 = Student('Good', 75, 'Japen')
print(f'ชื่อ {student01.fullname}')
print(f'คะแนน{student01.score}')
student01.checkGrade()
print('===============')
student02 = Student('exally', 90, 'Japen')
print(f'ชื่อ {student02.fullname}')
print(f'คะแนน{student02.score}')
student02.checkGrade()
print('===============')
student03 = Student('Should Imporve', 45, 'Japen')
print(f'ชื่อ {student03.fullname}')
print(f'คะแนน{student03.score}')
student03.checkGrade()
