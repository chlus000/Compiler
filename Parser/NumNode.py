from Parser.Node import Node

class NumNode(Node):
    def __init__(self, node):
        self.node=node
    
    def Print(self,sp):
        return ('   '*sp+str(self.node.num))