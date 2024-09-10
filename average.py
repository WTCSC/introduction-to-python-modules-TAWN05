import text_utils
import math
def average_words():
    # Defines file = opening and read mode of 'sample.txt'.
    file = open('sample.txt', 'r')
    # Defines text = the context of file.
    text = file.read()
    # Defines num _words = to the text_utils function count_words in context of text.
    num_words = text_utils.count_words(text)
    # Defines nlines = to the text_utils function count_lines in context of text.
    nlines = text_utils.count_lines(text)
    # Defines average = to num_words divided by nlines.
    average = (num_words / nlines) 
    # Defines round_average = to the floor or rounded down of the varable. 
    round_average = math.floor(average)
    # Closes the file that has been opened in the function.
    file.close()
    # Returns the formatted string (the desired output for average_words).
    return f'Average words per line: {round_average}'
# Call's average_words so it can be tested and prints the resault in terminal.
print(average_words())