from prettytable import PrettyTable
from collections import defaultdict
import os

class Repository:
    """Creates a complete summary of the students and teachers"""
    def __init__(self, directory, create_prettytables = False):
        self.students = PrettyTable(field_names= ["CWID", "Name", "Completed Courses"])
        self.instructors = PrettyTable(field_names= ["CWID", "Name", "Dept", "Course", "Students"])
        try:
            os.chdir(directory)
        except FileNotFoundError:
            raise NotADirectoryError ("Please provide a valid directory")
        self.stud_dict = {}     #dict with Keys = CWID, Values = instances of the Student object
        self.instr_dict = {}    #dict with Keys = CWID, Values = instances of the Instructor object
        self.create_studentsummary()
        self.create_instructorsummary()
        self.create_grades()
        if create_prettytables == True:
            self.create_pretty_tables()
    
    def read_files(self, file_name, expec_num_values, error_mess, seperator = "\t"):
        """A generic read file generator to check bad file inputs and read line by line"""
        try:
            fp = open(file_name, 'r')
        except FileNotFoundError:
            raise FileNotFoundError ("Could not open {}".format(file_name))
        else:
            with fp:
                for line in fp:
                    l = line.strip().split(seperator)
                    if len(l) == expec_num_values:
                        yield l
                    else:
                        raise ValueError (error_mess)

    def create_studentsummary(self):
        """This function creates all students and populates the student dictionary"""
        read_stud_file = self.read_files("students.txt", expec_num_values = 3, error_mess = "Please pass in only CWID, name, major", seperator = "\t", )
        for cwid, name, major in read_stud_file:
            s = Student(cwid, name, major)
            self.stud_dict[s.cwid] = s
        return None
    
    def create_instructorsummary(self):
        """This function creates all instructors and populates the instructor dictionary"""
        read_inst_file = self.read_files("instructors.txt", expec_num_values = 3, error_mess = "Please pass in only CWID, name, dept", seperator = "\t", )
        for cwid, name, dept in read_inst_file:
            i = Instructor(cwid, name, dept)
            self.instr_dict[i.cwid] = i
        return None

    def create_grades(self):
        """This function adds all information to instructors and students from the grades file"""
        read_grade_file = self.read_files("grades.txt", expec_num_values = 4, error_mess = "Please pass in only CWID, course, grade, instructor", seperator = "\t", )
        for s_cwid, course, grade, i_cwid in read_grade_file:
            if s_cwid in self.stud_dict:
                self.stud_dict[s_cwid].grades(course, grade)
            else:
                raise ValueError ("The student, CWID: {}, was not in the student file!".format(s_cwid))
            if i_cwid in self.instr_dict:
                self.instr_dict[i_cwid].grades(course)
            else:
                raise ValueError ("The instructor, CWID: {}, was not in the instructor file!".format(i_cwid))
        return None

    def create_pretty_tables(self):
        """This function creates and prints the pretty tables for view data nicely"""
        for stud in self.stud_dict.values():
            courses = list(stud.stud_course_grades.keys())
            self.students.add_row([stud.cwid, stud.name, sorted(courses)])
        for inst in self.instr_dict.values():
            for course in inst.instructor_courses:
                self.instructors.add_row([inst.cwid, inst.name, inst.dept, course, inst.instructor_courses[course]])
        print (self.students)
        print (self.instructors)
        return None


class Student:
    """Creates a summary of a student, tracking there CWID, name, major, completed courses, and grades"""
    def __init__(self, cwid, name, major):
        self.cwid = cwid
        self.name = name
        self.major = major
        self.stud_course_grades = defaultdict(str)
    
    def grades(self, course, grade):
        """This method creates a dictionary of courses taken and grade recieved"""
        self.stud_course_grades[course] = grade
        return None
        

class Instructor:
    """This class creates a summary of teachers, tracking there CWID, name, dept, course, and number of students"""
    def __init__(self, cwid, name, dept):
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.instructor_courses = defaultdict(int)
    
    def grades(self, course):
        """This method creates a dictionary of courses taught and number of students"""
        self.instructor_courses[course] += 1
        return None
        

def main():
    stevens_repository = Repository("Data Repository", True)


if __name__ == '__main__':
    main()