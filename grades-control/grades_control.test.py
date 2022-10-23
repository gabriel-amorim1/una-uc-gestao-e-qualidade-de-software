import unittest

from grades_control import SchoolSubject, Student

class GradesControlTest(unittest.TestCase):
  def test_create_student(self):
    student = Student("Gabriel", [10, 20])
    self.assertEqual(student.name, "Gabriel")
    self.assertEqual(student.grades, [10, 20])

  def test_school_subject(self):
    firstStudent = Student("Gabriel", [10, 20])
    secondStudent = Student("Luiz", [30, 50])

    schoolSubject = SchoolSubject("Matemática", [firstStudent, secondStudent])
    
    self.assertEqual(schoolSubject.name, "Matemática")
    self.assertEqual(schoolSubject.students[0], firstStudent)
    self.assertEqual(schoolSubject.students[1], secondStudent)

if __name__ == '__main__':
    unittest.main()