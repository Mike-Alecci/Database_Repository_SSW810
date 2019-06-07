import unittest
from collections import defaultdict
from collections import Counter

def anagram(str1, str2):
    """This function checks to see if str1 and str2 are anagrams by sorting a list
       of there characters and comparing them"""
    return sorted(list(str1)) == sorted(list(str2))

def anagram_dd(str1, str2):
    """This function checks to see if str1 and str2 are anagrams using a default dictionary"""
    dd = defaultdict(int)
    for elem in str1:
        dd[elem] += 1
    for check in str2:
        if check not in dd:
            return False
        else:
            dd[check] -= 1
    if any(dd.values()) == False:
        return True
    return False

def anagram_counters(str1, str2):
    """This function checks to see if str1 and str2 are anagrams using counters"""
    return Counter(str1) == Counter(str2)

def covers_alphabet(sentence):
    """This function checks to see if the given sentence has an instance of every letter in the alphabet"""
    s = set(sentence.lower())
    s1 = set('abcdefghijklomnopqrstuvwxyz')
    if s1 <= s:
            return True
    return False

def book_index(words):
    """This function returns a dictionary of all the words and their locations in a given book.
       In alphabetical and ascending order"""
    index = defaultdict(set)
    for element in words:
        index[element[0]].add(element[1])
    return sorted([[x, sorted(list(index[x]))] for x in index])

class MichaelsHomeworkTest(unittest.TestCase):
    """Tests that my homework works properly"""

    def test_anagram(self):
        """Tests that the anagram function works properly"""
        self.assertTrue(anagram('cinema', 'iceman'))
        self.assertTrue(anagram('dormitory', 'dirtyroom'))
        self.assertFalse(anagram('hello', 'world'))
        self.assertTrue(anagram('', ''))

    def test_anagram_dd(self):
        """Tests that the anagram_dd function works properly"""
        self.assertTrue(anagram_dd('cinema', 'iceman'))
        self.assertTrue(anagram_dd('dormitory', 'dirtyroom'))
        self.assertFalse(anagram_dd('hello', 'world'))
        self.assertTrue(anagram_dd('', ''))

    def test_anagram_counters(self):
        """Tests that the anagram_counters function works properly"""
        self.assertTrue(anagram_counters('cinema', 'iceman'))
        self.assertTrue(anagram_counters('dormitory', 'dirtyroom'))
        self.assertFalse(anagram_counters('hello', 'world'))
        self.assertTrue(anagram_counters('', ''))

    def test_covers_alphabet(self):
        """Tests that the covers alphabet function works properly"""
        self.assertTrue(covers_alphabet('abcdefghijklomnopqrstuvwxyz'))
        self.assertTrue(covers_alphabet('aabbcdefghijklomnopqrstuvwxyzzabc'))
        self.assertTrue(covers_alphabet('The quick brown fox jumps over the lazy dog'))
        self.assertTrue(covers_alphabet('We promptly judged antique ivory buckles for the next prize'))
        self.assertFalse(covers_alphabet(''))
        self.assertFalse(covers_alphabet('Should Fail'))

    def test_book_index(self):
        """Tests that the book_index method works properly"""
        l = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1),
            ('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2),
            ('could', 2), ('chuck', 1), ('wood', 1)]
        check = book_index(l)
        answer =  [['a', [1]], ['chuck', [1, 3]], ['could', [2]], ['how', [3]], ['if', [1]], ['much', [3]],
              ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]]
        for i in range(len(answer)):
            self.assertTrue(answer[i] == check[i])

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)