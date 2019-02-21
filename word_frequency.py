import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def new_text_file(text):
    """take a file, get unique words, turn them into all lowercase, no puncs, replace all whitespace with 1space. """

    text = text.casefold()
    valid_chars = string.ascii_letters + string.whitespace + string.digits

    # remove punc
    new_text = ""
    for char in text:
        if char in valid_chars:
            new_text += char

    text = new_text
    text = text.replace("\n", " ")
    return text


def unique_words(file):
    """Read in `file` and print out the frequency of words in that file."""

    with open(file) as file: 
        text = file.read()

    text = new_text_file(text)
    words = []
    for word in text.split(" "):
        if word != '' and word not in STOP_WORDS: 
            words.append(word)
    
    return words

def word_freq(words):
    """take list of words and count frequency"""
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    return word_count


# print(unique_words("seneca_falls.txt"))
# print("  ".join(unique_words("seneca_falls.txt")))
word_count = word_freq(unique_words("seneca_falls.txt"))
print(word_count)