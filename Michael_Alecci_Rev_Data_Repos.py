from prettytable import PrettyTable
from collections import defaultdict
import os
import radon

class Repository:
    """Creates a complete summary of the students and teachers"""
    def __init__(self, directory, create_prettytables = False):
        self.students = PrettyTable(field_names= ["CWID", "Name", "Completed Courses", "Remaining Required", "Remaining Electives"])
        self.instructors = PrettyTable(field_names= ["CWID", "Name", "Dept", "Course", "Students"])
        self.majors = PrettyTable(field_names = ["Dept", "Required Courses", "Electives"])
        try:
            os.chdir(directory)
        except FileNotFoundError:
            raise NotADirectoryError ("Please provide a valid directory")
        self.stud_dict = {}     #dict with Keys = CWID, Values = instances of the Student object
        self.instr_dict = {}    #dict with Keys = CWID, Values = instances of the Instructor object
        self.major_courses = defaultdict(set)      #default dict with keys = majors, Values = sets of courses
        self.major_electives = defaultdict(set)    #default dict with keys = majors, Values = sets of electives
        self.create_studentsummary()
        self.create_instructorsummary()
        self.create_grades()
        self.analyze_majors()
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

    def analyze_majors(self):
        """This function adds all of the information to students from the majors file"""
        read_majors_file = self.read_files("majors.txt", expec_num_values = 3, error_mess = "Please pass in only major, flag, and course", seperator = "\t")
        for major, flag, course in read_majors_file:
            if flag == "R":
                self.major_courses[major].add(course)
            elif flag == "E":
                self.major_electives[major].add(course)
            else:
                raise ValueError ("Please provide a proper flag")
        for stud in self.stud_dict.values():
            stud.majors(self.major_courses, self.major_electives)
        return None 

    def create_pretty_tables(self):
        """This function creates and prints the pretty tables for view data nicely"""
        for stud in self.stud_dict.values():
            if len(stud.remaining_electives) != len(self.major_electives[stud.major]):
                rem_elecs = "None"
            else:
                rem_elecs = stud.remaining_electives
            if len(stud.passed_courses) == 0:
                completed_courses = "None"
            else:
                completed_courses = stud.passed_courses
            self.students.add_row([stud.cwid, stud.name, completed_courses, stud.remaining_courses, rem_elecs])
        for inst in self.instr_dict.values():
            for course in inst.instructor_courses:
                self.instructors.add_row([inst.cwid, inst.name, inst.dept, course, inst.instructor_courses[course]])
        for major in self.major_courses.keys():
            self.majors.add_row([major, self.major_courses[major], self.major_electives[major]])
        print (self.majors)
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
        self.remaining_courses = set()
        self.remaining_electives = set()  
        self.passed_courses = set()
    
    def grades(self, course, grade):
        """This method creates a dictionary of courses taken and grade recieved"""
        self.stud_course_grades[course] = grade
        return None

    def majors(self, major_courses, major_electives):
        """This method creates two lists of remaining courses and electives for each student based off major"""
        if self.major in major_courses.keys():
            for course in self.stud_course_grades:
                if self.stud_course_grades[course] in {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}:
                    self.passed_courses.add(course)       #populates a set of courses passed
            self.remaining_courses = major_courses[self.major].difference(self.passed_courses)
            self.remaining_electives = major_electives[self.major].difference(self.passed_courses)
        else:
            raise ValueError ("This students major does not exist in the majors file!")
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