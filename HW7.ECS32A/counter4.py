#Homework 7 counter4.py
#Liana Williams
#
#Cleaning Words **Fix output**

import string

class Counter:
    def __init__(self):
        # Print a message indicating the object is being initialized
        print("Word Counter Initialized")
        
        # Initialize word_counts to an empty dictionary
        self.word_counts = {}

    def add_word(self, word):
        # Increment the count for the given word
        self.word_counts[word] = self.word_counts.get(word, 0) + 1

    def get_num_words(self):
        # Return the number of unique words or "None" if no words are present
        return len(self.word_counts)

    def increment_count(self, word):
        # Clean the word argument
        word = word.lower().strip(string.punctuation)
        
        # Return if the word is an empty string
        if not word:
            return

        # Increment or add the count for the cleaned word
        self.word_counts[word] = self.word_counts.get(word, 0) + 1

    def lookup_count(self, word):
        # Return the count for the given word, or 0 if not present
        return self.word_counts.get(word, 0)

# Test the Counter class
counter = Counter()

# Test increment_count and lookup_count methods
counter.increment_count("apple")
print(counter.lookup_count("apple"))  # Output: 1

counter.increment_count("banana")
print(counter.lookup_count("banana"))  # Output: 2

print(counter.lookup_count("grape"))  # Output: 0
print(counter.lookup_count("orange"))  # Output: 0

counter.increment_count("grape")  # Increment count for "grape"
counter.increment_count("orange")  # Increment count for "orange"
print(f"Unique words: {counter.get_num_words()}")
