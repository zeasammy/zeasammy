text = 'hi there hi hi hi !!!'
def word_replace():
    word_to_be_replaced=input('word to be replaced: ')
    word_replacement=input('word used as a replacement: ')
    print(text.replace(word_to_be_replaced, word_replacement))
word_replace()