from Parser.Node import Node

class BiOpNode(Node):
    def __init__(self, op_lexeme, left, right):
        self.op=op_lexeme.lexeme
        self.left = left
        self.right = right
    
    def Print(self, sp):
        right = self.right.Print(sp+1)
        left = self.left.Print(sp+1)
        return '   '*sp+str(self.op)+'\n'+str(left)+'\n'+str(right)