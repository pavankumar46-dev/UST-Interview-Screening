import unittest
from word_frequency import WordFrequency

class WordFrequencyUnitTest(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(WordFrequency().find_word_frequency(""), [])

    def test_single_word(self):
        self.assertEqual(WordFrequency().find_word_frequency("hello"), [("hello", 1)])

    def test_multiple_words(self):
        self.assertEqual(WordFrequency().find_word_frequency("hello world hello"), 
                         [("hello", 2), ("world", 1)])

    def test_with_duplicates(self):
        self.assertEqual(WordFrequency().find_word_frequency("test test test"), 
                         [("test", 3)])

    def test_mixed_case(self):
        self.assertEqual(WordFrequency().find_word_frequency("Hello hello HELLO"), 
                         [("HELLO", 1), ("Hello", 1), ("hello", 1)])

    def test_with_punctuation(self):
        self.assertEqual(WordFrequency().find_word_frequency("hello, world! hello."), 
                         [("hello,", 1), ("hello.", 1), ("world!", 1)])

    def test_sorted_output(self):
        self.assertEqual(WordFrequency().find_word_frequency("banana apple banana orange"), 
                         [("apple", 1), ("banana", 2), ("orange", 1)])

if __name__ == "__main__":
    unittest.main()