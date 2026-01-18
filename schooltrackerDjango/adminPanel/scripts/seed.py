from adminPanel.models import Student, Teacher, Section, Lesson, Notes

def run():
    # Clear existing data
    Notes.objects.all().delete()
    Student.objects.all().delete()
    Teacher.objects.all().delete()
    Section.objects.all().delete()
    Lesson.objects.all().delete()

    # Create Sections
    section1 = Section.objects.create(grade=5, branch='A')
    section2 = Section.objects.create(grade=6, branch='B')

    # Create Lessons
    math = Lesson.objects.create(name='Mathematics')
    physics = Lesson.objects.create(name='Physics')

    # Create Teachers
    teacher1 = Teacher.objects.create(name='Alice', surname='Smith', birthDate='1980-05-15', lesson=math)
    teacher2 = Teacher.objects.create(name='Bob', surname='Johnson', birthDate='1975-09-20', lesson=physics)

    # Create Students
    student1 = Student.objects.create(no=1001, name='Charlie', surname='Brown', birthDate='2005-03-10', section=section1)
    student2 = Student.objects.create(no=1002, name='Daisy', surname='Miller', birthDate='2004-07-22', section=section2)

    # Create Notes
    Notes.objects.create(firstQuiz=85, secondQuiz=90, finalExam=88, student=student1, lesson=math)
    Notes.objects.create(firstQuiz=78, secondQuiz=82, finalExam=80, student=student2, lesson=math)
    Notes.objects.create(firstQuiz=85, secondQuiz=90, finalExam=88, student=student1, lesson=physics)
    Notes.objects.create(firstQuiz=78, secondQuiz=82, finalExam=80, student=student2, lesson=physics)

    print("Database seeded successfully.")