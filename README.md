# Description
Python program that playes Word Hunt, a game where players swipe words on a 4x4 board of letters. Users can use the program via React web app that connects to a Flask backend to input a board and visualize valid word paths. 
# How It Works
The `TrieNode` class enables the construction of Tries, and has the methods `add` and `contains`. On startup, every word from a list of words is added to the Trie. After a user types in all 16 letters in the grid and presses enter, a call is made to the Flask backend. The `solve` function takes in the 16 letters and constructs a graph, where each letter is a node that has edges to the eight surrounding letters. 

Next, the `search` function is called on all 16 nodes/letters, and outputs the valid words and the paths to get to those words. This function iterates through the Trie and graph together. If the current Trie node is marked (meaning it is the end of a word), then the current letter is appended to the `validWords` list and the current node number is appended to the `paths` list. Then, for every neighbor of the current graph node, if that node is unvisited and the letter is a child of the current Trie node, then the `search` function is recursively called on the graph neighbor node and Trie child node. The results of this recursive call are then appended to the `validWords` and `paths` list, with the current letter and node number added at the front. Finally, the function returns `validWords` and `paths`. 

Once the `search` function finishes running, the web app displays a dropdown of each possible word, and clicking on a word displays the path of how to form that word. 
# Demo
https://github.com/abeinn/wordhunt/assets/63220193/a6ec1aed-f31e-496b-a205-41a3b5aab06d

