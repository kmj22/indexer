import os
import re
from bs4 import BeautifulSoup

def frequencyInvertedIndex(documents):
    index = {}
    n = 0
    for document in documents:
        print("Indexing " + document)

        frequency = {}
        n += 1

        tokens = parse(document)
        
        for token in tokens:
            if token not in frequency:
                frequency[token] = 0

            frequency[token] += 1

        for key in frequency.keys():
            if key not in index:
                index[key] = []

            index[key].append([n, frequency[key]])

    return index

def positionInvertedIndex(documents):
    index = {}
    n = 0
    for document in documents:
        print("Indexing " + document)

        n += 1
        position = 1

        tokens = parse(document)
        
        for token in tokens:
            if token not in index:
                index[token] = []

            index[token].append([n, position])
            position += 1
        break

    return index

def parse(document):
    file = open(document, mode='r', encoding="utf8")
    soup = BeautifulSoup(file.read().lower(), 'html.parser') 
    file.close()

    for script in soup(["script", "style", "a"]):
        script.extract()

    text = soup.get_text()
    text = re.sub("[\.\']","", text)
    text = re.sub('[^a-z0-9\ \-]+', " ", text)

    return text.split()

def getDocuments():
    documents = []
    directory = os.getcwd() + "\\crawled-pages"
    
    for file in os.listdir(directory):
        if file.endswith(".html"):
            document = (os.path.join(directory, file))
            documents.append(document)

    return documents

documents = getDocuments()

index = frequencyInvertedIndex(documents)
#index = positionInvertedIndex(documents)

f = open('InvertedIndex.txt','w+')
f.write(str(index))
f.close()

f = open("Vocabulary.txt", "w+")
for word in index.keys():
    f.write(word + "\n")
f.close()
