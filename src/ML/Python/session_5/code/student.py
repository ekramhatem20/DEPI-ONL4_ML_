class Student:
    _id_counter = 1
    
    def __init__(self,name):
        self.student_id = Student._id_counter
        Student._id_counter += 1
        self.name = name
        self.grades = {}
        self.enrolled_courses = []
        
    def __repr__(self):
        return f"Student ID:{self.student_id}\nName:{self.name}\nGrades:{self.grades} "
         
    def add_grade(self,course_id,grade):
        self.grades[course_id] = grade 
        
    def enroll_in_courses(self,course):
        self.enroll_in_courses.append(course)      