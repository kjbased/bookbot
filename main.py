def main():
    book_path = "books/frankenstein.txt"
    text = bookText(book_path)
    wordCount = numWords(text)
    #print (text)
    print ("---------------------------")
    print (f"Total words: {wordCount}" )

def bookText(book_path):
    with open (book_path) as f:
        return f.read()

def numWords(text):
    words = text.split()
    return len(words)
main()