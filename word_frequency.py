
from collections import OrderedDict
import threading
import time

class WordFrequency:

    # Function which handles single input at a time
    def find_word_frequency(self, input_string):
        # To preserver the order and to remove duplicates
        unique_lst = list(OrderedDict.fromkeys(input_string.split()))
        freq_lst = []
        for value1 in unique_lst:
            counter = 0
            for value2 in input_string.split():
                if value1 == value2:
                    counter = counter + 1
                
            freq_lst.append((value1, counter))
            
        freq_lst.sort()
        for i in freq_lst:
            print(i)
        print("--- Done with execution ---")
        return freq_lst


    # Function which handles multiline input from file in parallel fashion
    def multi_thread_word_frequency(self):
        thread_lst = []
        file = open('./sample_inputs/word_frequency_input.txt')
        # Using multithreading to handle n lines of input in parallel
        for i in file.readlines():
            thread = threading.Thread(target=self.find_word_frequency, args=(i,))
            thread_lst.append(thread)
            thread.start()
            time.sleep(1)

        # Wait to threads to finish
        for thread in thread_lst:
            thread.join()

