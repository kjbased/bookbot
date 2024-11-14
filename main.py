def main():
    book_path = "books/frankenstein.txt"
    text = bookText(book_path)
    wordCount = numWords(text)
    letterCount = numLetters(text)
    sortedChars = sortedCount(letterCount)

    print (f"--- Begin Report of {book_path} ---")
    print (f"{wordCount} words found in the document")
    bookReport(sortedChars)
    print ("--- End Report ---") 

#function to open book file and return as a string
def bookText(book_path):
    with open (book_path) as f:
        return f.read()

#function to split book into individual words and return total number of words
def numWords(text):
    words = text.split()
    return len(words)

#function to count indivdual character and return how many times each character was used
def numLetters(text):
    letterCount = {}
    for chars in text:
        lowercase = chars.lower()
        if lowercase in letterCount:
            letterCount[lowercase] += 1
        else:
            letterCount[lowercase] = 1        
    return letterCount

#function to return sort key
def sortKey (sorted):
    return sorted['num']

#function to return sorted dictionary by frequency of letter appearance
def sortedCount (letterCount):
    sortedChars = []
    for letter in letterCount:
        isLetter = letter.isalpha()
        if isLetter == True: 
            tempDict = {"char": letter, "num": letterCount[letter]}
            sortedChars.append(tempDict)
    sortedChars.sort(reverse=True, key=sortKey)
    return (sortedChars)

#function to provide book summary of total words and how many times each letter was found
def bookReport (sortedChars):
    for letter in sortedChars:
            print (f"The '{letter['char']}' was found {letter['num']} times")
    return ()

main()