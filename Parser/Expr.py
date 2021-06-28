from Parser.NumNode import NumNode
from Parser.IdentNode import IdentNode
from Parser.BiOpNode import BiOpNode
from Lex_analyzer.Lexer import Lexer

class ExprParser():
    def __init__(self,test):
        self.lexer=Lexer(test)
    
    def ParseExpr(self):
        left=self.ParseTerm()
        op_lexeme=self.lexer.lex_getter()

        while op_lexeme.lexeme=='+' or op_lexeme.lexeme=='-':
            self.lexer.NewLex()
            right=self.ParseTerm()
            left=BiOpNode(op_lexeme,left,right)
            op_lexeme=self.lexer.lex_getter()
        return left



    def ParseTerm(self):
        left=self.ParseFactor()
        op_lexeme=self.lexer.lex_getter()

        while op_lexeme.lexeme=='*' or op_lexeme.lexeme=='/':
            self.lexer.NewLex()
            right=self.ParseFactor()
            left=BiOpNode(op_lexeme,left,right)
            op_lexeme=self.lexer.lex_getter()
        return left


    def ParseFactor(self):
        self.lexeme=self.lexer.lex_getter()
        self.lexer.NewLex()
        if self.lexeme.type=='Integer' or self.lexeme.type=='Real':
            return NumNode(self.lexeme)
        if self.lexeme.type=='Identifier':
            return IdentNode(self.lexeme)
        if self.lexeme.lexeme=='(':
            left=self.ParseExpr()
            self.lexeme=self.lexer.lex_getter()
            if self.lexeme.lexeme!=')':
                raise Exception(') expected')
            self.lexeme=self.lexer.NewLex()
            return left

