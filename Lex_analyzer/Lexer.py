from Lex_analyzer.Lexeme import Lexeme
from Lex_analyzer.States import State
from Lex_analyzer.Analyzer import Analyzer

class Lexer:
    def __init__(self,test):
  
        self.test = open(test, 'r', encoding="utf-8")
        self.line,self.pos=1,1
        self.start_pos_lex,self.line_lex=0,0  
        self.ch=self.test.read(1)
        self.next_ch=self.test.read(1)
        self.type,self.buff='',''
        self.state='S'
        self.newstate=''
        self.num=''
        self.all_states=State()
        self.analyze=Analyzer()
        

    def NewLex(self):
        self.newstate='S'
        while self.newstate!='F' and self.newstate!='Err':
            self.state=self.newstate
            if self.state=='S':
                self.buff_clear()
                self.get_start_lex()
            if not self.double_point_check():
                self.newstate=self.all_states.GetNextState(self.ch,self.state)
            if self.newstate!='F':
                self.add_to_buff()
                self.next_char()
        self.state=self.analyze.type_getter(self.newstate,self.state,self.buff)
        self.num=self.analyze.checking_num(self.state,self.buff)
        if self.state == "Error":
            return Lexeme(self.line_lex, self.start_pos_lex,self.state,self.buff,'',True)
        else:
            return Lexeme(self.line_lex, self.start_pos_lex,self.state,self.buff,self.num, False)


    def next_char(self):
        self.ch=self.next_ch
        self.next_ch = self.test.read(1)
        self.pos+=1
        if self.ch=='\n':
            self.line+=1
            self.pos=0

    def add_to_buff(self):
        self.buff+=self.ch

    def buff_clear(self):
        self.buff=''

    def get_start_lex(self):
        self.start_pos_lex=self.pos
        self.line_lex=self.line
        

    def double_point_check(self):
        if self.ch=='.' and self.next_ch=='.' and self.buff!='' and (self.state=='Delim' or self.state=='Int'):
            self.newstate='F'
            return True
        else:
            return False
    
    def lex_getter(self):
        if self.buff:
            return Lexeme(self.line_lex, self.start_pos_lex,self.state,self.buff,self.num, False)
        else:
            return self.NewLex()