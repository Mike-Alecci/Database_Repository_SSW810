import unittest

def count_dist_vals(seq):
    """This creates a list of lists where each inner list is a pair
       of the unique values in s and the number of occurrences of each value."""
    distinct = list()
    for element in seq:
        if [element, seq.count(element)] not in distinct:
            distinct.append([element, seq.count(element)])
    return distinct

def remove_vowels(s):
    """This function returns a list containing all values of a passed in string except the vowels"""
    return "".join([element for element in list(s) if element.lower() not in "aeiou"])

def insertion_sort(L):
    """This function returns a copy of a list in a sorted least to greatest order"""
    new_list = list()
    for i in range(len(L)):
        for v in range(len(new_list)):
            if L[i] <= new_list[v]:
                new_list.insert(v, L[i])
                break                       #We want to stop as soon as we have found the right location
        else:
            new_list.append(L[i])           #This covers the first value and any temporary largest values
    return new_list

class MichaelsHomeworkTest(unittest.TestCase):
    """Tests that my homework works properly"""

    def test_count_dist_vals(self):
        """Tests that the count_dist_vals function works properly"""
        self.assertEqual(count_dist_vals("Mississippi"), [["M", 1], ["i", 4], ["s", 4], ["p", 2]])
        self.assertEqual(count_dist_vals("      "), [[" ", 6]])
        self.assertEqual(count_dist_vals("Test stuff"), [["T", 1], ["e", 1], ["s", 2], ["t", 2], [" ", 1], ["u", 1], ["f", 2]])
        self.assertEqual(count_dist_vals(["M", "i", "s", "s", "i"]), [["M", 1], ["i", 2], ["s", 2]])
        self.assertEqual(count_dist_vals([""]), [["", 1]])

    def test_remove_vowels(self):
        """Tests that the remove_vowels function works properly"""
        self.assertEqual(remove_vowels("HeLlo WoRld"), "HLl WRld")
        self.assertEqual(remove_vowels("Time to test more"), "Tm t tst mr")
        self.assertEqual(remove_vowels(""), "")
        self.assertEqual(remove_vowels("     "), "     ")
        self.assertEqual(remove_vowels("123aeiou"), "123")

    def test_insertion_sort(self):
        """Tests that the insertion sort function works properly"""
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort([5, 44, 33, 2, 13]), [2, 5, 13, 33, 44])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort([-5, 4, -3, 2, 1]), [-5, -3, 1, 2, 4])

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)