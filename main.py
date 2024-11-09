from word_frequency import WordFrequency
from word_frequency_unit_test import WordFrequencyUnitTest
import unittest

# Object creation
word_frequency_obj = WordFrequency()
unit_test_word_frequency_obj = WordFrequencyUnitTest()

# Single word frequency function call
word_frequency_obj.find_word_frequency("Testing sample input")
print("Done with Single word frequency function call")
print("============================================")

# Multithreading implementation function call
word_frequency_obj.multi_thread_word_frequency()
print("Done with Multithreading implementation function call")
print("============================================")

# Unit test implementation call
suite = unittest.TestLoader().loadTestsFromTestCase(WordFrequencyUnitTest)

test_runner = unittest.TextTestRunner()
result = test_runner.run(suite)

print(f"Tests run: {result.testsRun}")
print(f"Failures: {len(result.failures)}")
print(f"Errors: {len(result.errors)}")

