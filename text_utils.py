def count_chars(text):
    return len(text)


def count_words(text):
    return len(text.split())
    
def count_sentences(text):
    i = text.count('.')
    b = text.count('!')
    a = text.count('?')
    num_sentences = (i + b + a)
    return num_sentences

def count_lines(text):
    return text.count('\n')