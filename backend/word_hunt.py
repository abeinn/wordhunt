from TrieNode import TrieNode
from Graph import Graph
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "words.txt")) as f:
    words = map(lambda s: s.strip(), f.readlines())

MIN_LEN = 3
MAX_LEN = 25

root = TrieNode()
for word in words:
    if MIN_LEN <= len(word) <= MAX_LEN:
        root.add(word)

# Return a mapping of valid words to the path to form the word
def solve(letters: str):
    length = len(letters)
    gridSize = int(length ** 0.5)

    g = Graph(length)

    for i in range(length):
        indices = [i + gridSize, i - gridSize]
        if i % gridSize != 0:
            indices.extend([i - 1, i - gridSize - 1, i + gridSize - 1])
        if i % gridSize != gridSize - 1:
            indices.extend([i + 1, i - gridSize + 1, i + gridSize + 1])
        for j in indices:
            if j >= 0 and j < length:
                g.addEdge(i, j)

    wordToPath = {}
    for i in range(length):
        visited = [False] * length
        validWords, paths = search(letters, g, i, root.children[letters[i]], visited)
        for word, path in zip(validWords, paths):
            wordToPath[word] = path

    sortedWords = sorted(wordToPath.keys(), key=len, reverse=True)
    output = []
    id = 0
    for w in sortedWords:
        output.append({"id": id, "word": w, "path": wordToPath[w]})
        id += 1
    return output


def search(letters:str, g: Graph, v: int, t: TrieNode, visited: list):
    visited[v] = True
    validWords = []
    paths = []
    currChar = letters[v]
    if t.marked:
        validWords.append(currChar)
        paths.append([v])

    for w in g.adj[v]:
        nextChar = letters[w]
        if not visited[w] and nextChar in t.children:
            x = search(letters, g, w, t.children[nextChar], visited[:])
            for word, path in zip(x[0], x[1]):
                validWords.append(currChar + word)
                paths.append([v] + path)
            
    return validWords, paths
