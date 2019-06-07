import unittest

def rev_string(str_input):
    """This function takes in a string input and returns the reverse of the string"""
    new_str = "" 
    for i in range(len(str_input)-1, -1, -1):
        new_str += str_input[i]
    return new_str

def rev_enumerate(seq):
    """This generator returns a string in backwards order with the proper offset to each character assigned"""
    for offset in range(len(seq)-1, -1, -1):
        yield offset, seq[offset]

def check_palindrome(value):
    """This checks if a string is a palindrome by checking the first char to the last
       and moves in stopping at halfway. This is programmed for efficiency when a string is not a palindrome"""
    answer = True
    value = value.lower()
    for i in range(int(len(value)/2)):
        if value[i] != value[-1-i]:
            answer = False
            break                       #no need to continue if the answer is false
    return answer

def find_second(s1, s2):
    """Returns the index of the second index of a target string in a string, returns -1 if it doesn't exist.
       This Function is intentionally case sensitive"""
    return s2.find(s1, s2.find(s1)+1)

def remove_th(s):
    """This function removes any words that begin with a th in a string, in any variation of caps or lowercase
       and then returns a new string with the remaining words and trailing/ending white spaces stripped"""
    unchanged = s.split()
    answer = ""
    for i in unchanged:
        if i[0:2].lower() != "th" and i[len(i)-2:].lower() != "th":
            answer += i + " "
    return answer.strip() 

def covers_alphabet(check):
    """This function checks to see if every letter in the alphabet is contained within a given sentence"""
    answer = True
    check = check.lower()
    for letter in "abcdefghijklomnopqrstuvwxyz":
        if letter not in check:
            answer = False
            break                   #no need to continue if any letter is not contained
    return answer
    
class MichaelsHomeworkTest(unittest.TestCase):
    """Tests that my homework works properly"""

    def test_check_palindrome(self):
        """Tests the check_palindrome function works properly"""
        self.assertTrue(check_palindrome("racecar"))
        self.assertTrue(check_palindrome("raccar"))
        self.assertFalse(check_palindrome("racebike"))
        self.assertTrue(check_palindrome("12321"))
        self.assertTrue(check_palindrome("1"))
        self.assertTrue(check_palindrome(""))

    def test_rev_string(self):
        """Tests the rev_string function works properly"""
        self.assertEqual(rev_string("python"), "nohtyp")
        self.assertEqual(rev_string("12345"), "54321")
        self.assertEqual(rev_string(""), "")
    
    def test_rev_enumerate(self):
        """Tests the rev_enumerate function works properly"""
        check = ["5 n", "4 o", "3 h", "2 t", "1 y", "0 p"]
        x=0
        for i, v in rev_enumerate("python"):
            self.assertEqual(str(i) + " " + str(v), check[x])
            x += 1

    def test_find_second(self):
        """Tests that the find_second function works properly"""
        self.assertEqual(find_second("iss", "Mississippi"), 4)
        self.assertEqual(find_second("ix", "Mississippi"), -1)
        self.assertEqual(find_second("s", "Mississippi"), 3)
        self.assertEqual(find_second("Iss", "Mississippi"), -1)
        self.assertEqual(find_second("1", "111111"), 1)
    
    def test_remove_th(self):
        """Tests that the remove_th function works properly"""
        self.assertEqual(remove_th(" HeLLo This THat tHere tootH WoRlD"), "HeLLo WoRlD")
        self.assertFalse(remove_th("HeLLo This THat tHere tootH WoRlD") == " HeLLo WoRlD ")
        self.assertEqual(remove_th("hi"), "hi")
        self.assertEqual(remove_th("Nothtoremove except this1"), "Nothtoremove except")
        self.assertEqual(remove_th(""), "")
        self.assertEqual(remove_th("th thdfg dsgth"), "")

    def test_covers_alphabet(self):
        """Tests that the covers_alphabet function works properly"""
        self.assertTrue(covers_alphabet("abcdefghijklomnopqrstuvwxyz"))
        self.assertTrue(covers_alphabet("aabbcdefghijklomnopqrstuvwxyzzabc"))
        self.assertTrue(covers_alphabet("The quick brown fox jumps over the lazy dog"))
        self.assertTrue(covers_alphabet("We promptly judged antique ivory buckles for the next prize"))
        self.assertFalse(covers_alphabet(""))
        self.assertFalse(covers_alphabet("erf34"))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)