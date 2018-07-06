
import unittest
from TestingClassTestCases.phonebook import Phonebook

class PhonebookTest(unittest.TestCase):
    """This PhonebookTest class is denominated as a text file fixture which indicate that
    all of the testcase belongs to this testsuite. will edit this comment as we move forward."""

    def setUp(self):
        self.phonebook = Phonebook()

    # This is testcase 1, will be commented since the setUp method will take care of this method each time that a test case is executed.
    """def test_create_phonebook(self):
        phonebook = Phonebook()"""

    # This is testcase 2
    def test_lookup_entry_by_name(self):
        self.phonebook.add("Bob", "12345")
        self.assertEquals("12345", self.phonebook.lookup("Bob"))
    #This is test case 3
    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")
   # @unittest.skip("WIP") # <-- will make the test runner to skip the test.
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    """Below is a good example of how should testing be small and consistent"""
    def test_phonebook_with_normal_entries_is_inconsistent(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_inconsistent(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Mary", "12345")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Mary", "123")
        self.assertFalse(self.phonebook.is_consistent())