from TrieNode import TrieNode
from Graph import Graph
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "words.txt")) as f:
    words = map(lambda s: s.strip(), f.readlines())

MAX_LEN = 25

root = TrieNode()
for word in words:
    if len(word) <= MAX_LEN:
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

    output = {}
    for i in range(length):
        visited = [False] * length
        validWords, paths = search(letters, g, i, root, visited)
        for word, path in zip(validWords, paths):
            output[word] = path

    return dict(sorted(output.items(), key=lambda item: len(item[0]), reverse=True))

def search(letters:str, g: Graph, v: int, t: TrieNode, visited: list):
    visited[v] = True
    validWords = []
    paths = []
    if t.marked:
        validWords.append("")
        paths.append([])

    for w in g.adj[v]:
        if not visited[w] and letters[w] in t.children:
            c = letters[w]
            x = search(letters, g, w, t.children[c], visited)
            for word, path in zip(x[0], x[1]):
                validWords.append(c + word)
                paths.append([w] + path)
            
    return validWords, paths
