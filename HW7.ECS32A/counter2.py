#Homework 7 counter2.py
#Liana Williams
#
#Complete get_num_words method

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

# Test the Counter class
counter = Counter()
print(f"Unique words: {counter.get_num_words()}")
