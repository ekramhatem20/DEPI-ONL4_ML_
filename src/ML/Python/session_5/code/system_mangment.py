from student import Student
from course import Course

"""



"""
class SystemManger:
    
    def __init__(self):
        self.students = {}
        self.courses = {}
        
    def add_student(self,name):
        student = Student(name)
        self.students[student.student_id] = name
        print("Student added successfuly")
        return student.student_id
    
    def remove_student(self,student_id):
        if student_id in self.students:
            student = self.students[student_id]
            if not student.enrolled_course:
                del self.students[student_id]
                print("Student removed sucessfully")
            else:
                print("Student has enrolled courses . cannot remove ")
        else:
            print("Invalid student ID")     
            
            
    def add_course(self,name):
        course = Course(name)
        self.courses[course.course_id] = course   
        print("Course added successfully!")
        return course.course_id
    
    
    def remove_course(self,course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            if not course.enrolled_students:
                del self.courses[course_id]
                print("Course removes")
            else:
                print("can not remove")
        else:
            print("Invalid course ID")