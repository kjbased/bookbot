def main():
    book_path = "books/frankenstein.txt"
    text = bookText(book_path)
    wordCount = numWords(text)
    letterCount = numLetters(text)

    #print (text)
    print ("---------------------------")
    print (f"Total words: {wordCount}" )
    print ("---------------------------")
    print (letterCount)

def bookText(book_path):
    with open (book_path) as f:
        return f.read()

def numWords(text):
    words = text.split()
    #print (words)
    return len(words)

def numLetters(text):
    letterCount = {}
    for chars in text:
        lowercase = chars.lower()
        if lowercase in letterCount:
            letterCount[lowercase] += 1
        else:
            letterCount[lowercase] = 1        
    return letterCount
    pass

main()