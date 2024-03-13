#Homework 7 counter7.py
#Liana Williams
#
#Find and return the most frequent words
import string

class Counter:
    def __init__(self):
        # Print a message indicating the object is being initialized
        print("Word Counter Initialized")

        # Initialize word_counts to an empty dictionary
        self.word_counts = {}

        # Initialize stop_words to an empty list
        self.stop_words = []

        # Read stop words from the file and store them in the list
        with open("stop_words.txt", 'r', encoding='utf-8') as stop_words_file:
            for stop_word in stop_words_file:
                self.stop_words.append(stop_word.strip())

    def add_word(self, word):
        # Increment the count for the given word
        self.word_counts[word] = self.word_counts.get(word, 0) + 1

    def get_num_words(self):
        # Return the number of unique words or "None" if no words are present
        return len(self.word_counts)

    def increment_count(self, word):
        # Clean the word argument
        word = word.lower().strip(string.punctuation)

        # Return if the word is an empty string or a stop word
        if not word or word in self.stop_words:
            return

        # Increment or add the count for the cleaned word
        self.word_counts[word] = self.word_counts.get(word, 0) + 1

    def lookup_count(self, word):
        # Return the count for the given word, or 0 if not present
        return self.word_counts.get(word, 0)

    def get_top_words(self, num):
        # Create a list of tuples from the dictionary items
        word_tuples = [(count, word) for word, count in self.word_counts.items()]

        # Sort the list in reverse order based on count
        word_tuples.sort(reverse=True)

        # Return the first "num" elements from the sorted list
        return word_tuples[:num]

# Test the Counter class
counter = Counter()

# Uncomment the test code for Part 7
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

# Uncomment the test code for Part 7
top_words = counter.get_top_words(10)
print("Top 10 Words:")
print(top_words)
print(f"Unique words: {counter.get_num_words()}")
