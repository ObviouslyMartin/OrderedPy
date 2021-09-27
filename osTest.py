if __name__ == '__main__':
    from orderedSet import *
    from wordData import *

    oneWord = WordData()
    wordSet = OrderedSet()
    with open("words.txt", "r") as inWords:
        c = inWords.read(1)
        
