import unittest
import os
from Michael_Alecci_Rev_Data_Repos import Repository
from Michael_Alecci_Rev_Data_Repos import Student
from Michael_Alecci_Rev_Data_Repos import Instructor

class MichaelsHomeworkTest(unittest.TestCase):
    """Tests that my homework works properly"""

    def test_bad_stuff(self):
        """This is made for testing things that could raise errors, ie an improper directory name, 
        bad file inputs, non existent files, grades with new students and instructors"""
        x = os.getcwd()
        self.assertRaises(NotADirectoryError, Repository, "Fake dir, I dont exist") #fake directory name
        self.assertRaises(ValueError, Repository, "New_data")  #has a new student and instructor in grades
        os.chdir(x)
        self.assertRaises(ValueError, Repository, "Bad studs inputs")   #has extra values in students file
        os.chdir(x)
        self.assertRaises(FileNotFoundError, Repository, "No files here")   #has no files in the directory
        os.chdir(x)
        
    def test_good_inputs(self):
        """This tests that my database is working properly"""
        path = os.getcwd()
        test_dict_stud = {"10103": Student("10103", "Baldwin, C", "SFEN"), "10115": Student("10115", "Wyatt, X", "SFEN")}
        test_dict_inst = {"98765": Instructor("98765", "Einstein, A", "SFEN"), "98764": Instructor("98764", "Feynman, R", "SFEN"), "98762": Instructor("98762", "Hawking, S", "SYEN")}
        x = Repository("test good inputs")
        self.assertEqual(x.stud_dict.keys(), test_dict_stud.keys())
        self.assertEqual(x.instr_dict.keys(), test_dict_inst.keys())
        os.chdir(path)

    def test_majors(self):
        """This tests that the analyze majors addition to the database works"""
        test_req_courses = {"SFEN": {"SSW 540"}, "SYEN": {"SYS 671"}}
        test_req_elecs = {"SFEN": {"CS 501"}, "SYEN": {"SSW 810"}}
        test = Repository("test good inputs")
        for key in test_req_courses.keys():
            self.assertEqual(test.major_courses[key], test_req_courses[key])
        for key in test_req_elecs.keys():
            self.assertEqual(test_req_elecs[key], test.major_electives[key])

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)