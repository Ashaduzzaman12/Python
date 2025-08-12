class Student:
    def __init__(self,name,id,Cls):
        self.name=name
        self.id=id
        self.classe=Cls

    def __repr__(self):
        return f'student with name :{self.name},class={self.classe}'
    

class teacher:
    def __init__(self,name,id,sub):
        self.name=name
        self.id=id
        self.sub=sub

    def __repr__(self):
        return f'teacher with name:{self.name},subject:self.sub'
class school:
    def __init__(self,name):
        self.name=name
        self.teacher=[]
        self.student=[]
        
    def add_teacher(self,name,subject):
        id=len(self.teacher)+101
        teachers=teacher(name,subject,id)
        self.teacher.append(teachers)
    
    def enroll(self,name,fee):
        if fee<6500:
            return 'not enough fee'
        else:
            id=len(self.student)+1
            students=Student(name,id,'c')
            self.student.append(students)


alia=Student('Alia misho',10,6)
print(alia)

sir=teacher('ranbeen',10,'math')
print(sir)
        