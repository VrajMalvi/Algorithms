# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
# O(v + e) time | O(v) space : v- vertices(node), e-edges 
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name) # append name of node
        for child in self.children:
            child.depthFirstSearch(array)
        return array
        
