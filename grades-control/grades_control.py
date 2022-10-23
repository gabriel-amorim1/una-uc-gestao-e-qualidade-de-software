class SchoolSubject:
    def __init__(self, name, students):
        self.name = name
        self.students = students

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
    def getName(self):
        return self.name
        
    def getGrades(self):
        return self.grades


def get_student(subjectName):
    registerStudentNameMessage = "Digite o nome do aluno: "

    studentName = input(registerStudentNameMessage)
    lst = list(map(float, input(("Digite as notas das provas de %s separadas por espaço: " % subjectName)).strip().split()))[:2]

    return Student(studentName, lst)
    

def get_school_subject():
    registerStudentMessage = "Tecle para registar aluno e -1 para finalizar: "
    registerSubjectNameMessage = "Digite o nome da matéria: "

    students = []

    subjectName = input(registerSubjectNameMessage)
    studentChoice = input(registerStudentMessage)
    
    while(studentChoice != "-1"):
        students.append(get_student(subjectName))
        studentChoice = input(registerStudentMessage)
    
    return SchoolSubject(subjectName, students)
    

def get_school_subjects():
    registerSubjectMessage = "Tecle para registar matéria e -1 para finalizar: "


    subjects = []


    subjectChoice = input(registerSubjectMessage)
    while(subjectChoice != "-1"):
        subjects.append(get_school_subject())
        subjectChoice = input(registerSubjectMessage)

    return subjects

def print_table(subjects):
    for subject in subjects:
        print("%s---------------------------------------------------------------------" % subject.name)
        print("Nome\t\t\tNota 1\t\t\tNota 2\t\t\tTotal\t\tSituação")    
        print("---------------------------------------------------------------------")
        for student in subject.students:
            grades = student.getGrades()
            total = sum(grades)
            
            if (total >= 60.0):
                situation = 'APROVADO'
            elif (total < 40.0):
                situation = 'REPROVADO'
            else:
                situation = 'RECUPERAÇÃO'
        
            print("%s:\t\t%s\t\t%s\t\t%s\t\t%s" % (student.getName(), grades[0], grades[1], "{:.1f}".format(total), situation ))
        print("---------------------------------------------------------------------")
        print("                                                                     ")

def grades_control():
    subjects = get_school_subjects()
    print_table(subjects)