#Homework 7 counter5.py
#Liana Williams
#
#Read the document and count the words


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

# Uncomment the test code for Parts 5 and 6
while True:
    file_name = input("Enter book file:")

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            # Process each line in the file
            for line in file:
                # Split the line into words using whitespace characters
                words = line.split()

                # Increment the count for each word
                for word in words:
                    counter.increment_count(word)
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Try again.")
    else:
        break

# Uncomment the test code for Parts 5 and 6
print(f"alice: {counter.lookup_count('alice')}")
print(f"rabbit: {counter.lookup_count('rabbit')}")
print(f"and: {counter.lookup_count('and')}")
print(f"she: {counter.lookup_count('she')}")
print(f"Unique words: {counter.get_num_words()}")
