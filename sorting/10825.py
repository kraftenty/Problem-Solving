import sys
input=sys.stdin.readline

class Student:
    def __init__(self, name, kor, eng, math):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
    def __lt__(self, other): # 객체 정렬을 위한 <(less than) 오버로딩
        if self.kor != other.kor:
            return self.kor < other.kor
        elif self.eng != other.eng:
            return self.eng > other.eng
        elif self.math != other.math:
            return self.math < other.math
        else:
            return self.name > other.name


n=int(input())
students=[]
for _ in range(n):
    name,kor,eng,math=input().split()
    students.append(Student(name,int(kor),int(eng),int(math)))

students.sort(reverse=True)
for student in students:
    print(student.name)