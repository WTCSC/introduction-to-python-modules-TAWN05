import text_utils
def average_words():
    num_words = text_utils.count_words('sample.txt')
    """nlines = text.count('\n')"""
    nlines = text_utils.count_lines('sample.txt')
    average = (num_words)/(nlines)
    message = (f'Average words per line: {average}')
    return message