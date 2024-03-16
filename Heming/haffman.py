"""Haffman algorithm."""

class Haffman:
    """Class of Haffman algorithm"""

    class Node:
        """Class of node of haffman algorithm"""

        def __init__(self, left, right):
            self.left = left
            self.right = right

    def __init__(self, text):
        letters = set(text)
        frequences = []
        for letter in letters:
            frequences.append((text.count(letter), letter))

        while len(frequences) > 1:
            frequences = sorted(frequences, key=lambda x: x[0], reverse=True)
            first = frequences.pop()
            second = frequences.pop()
            freq = first[0]+second[0]
            frequences.append((freq, self.Node(first[1], second[1])))

        self.code = {letter: '' for letter in letters}

        def walk(node, path=''):
            if isinstance(node, str):
                self.code[node] = path
                return
            walk(node.left, path + '0')
            walk(node.right, path + '1')
            
        walk(frequences[0][1])

    def get_codes(self):
        """Get result code"""
        return self.code
