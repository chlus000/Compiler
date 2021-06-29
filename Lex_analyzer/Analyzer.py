class Analyzer:
    def __init__(self):
        self.types={'Err':'Error',
                    'ErrSynt':'Syntax error',
                    'ErrStr':'Error: " \' " was expected',
                    'ErrStrCont':'Error: number was expected',
                    'S':'',
                    'StrEnd':'String',
                    'IntStr':'String',
                    'Int':'Integer',
                    'Point':'Integer',
                    'DoublePoint':'Delimiter',
                    'DoubleEnd':'Delimiter',
                    'Int2':'Integer',
                    'Int8':'Integer',
                    'Int16':'Integer',
                    'Slash':'Operator',
                    'Real':'Real',
                    'RealE':'Real',
                    'RealNum':'Real',
                    }
        self.key_words = {"and", "array", "as", "auto", "begin", "case", "class", "const", 
                        "constructor", "destructor", "div", "do", "downto", "else", "end", 
                        "event", "except", "extensionmethod", "file", "finalization", "finally", 
                        "for", "foreach", "function", "goto", "if", "implementation", "in", 
                        "inherited", "initialization", "interface", "is", "label", "lock", 
                        "loop", "mod", "nil", "not", "of", "operator", "or", 'Print', 'Println', "procedure", 
                        "program", "property", "raise", 'Read', 'Readln', "ReadReal", "record", "repeat", "sealed", "set", 
                        "sequence", "shl", "shr", "sizeof", "template", "then", "to", "try", 
                        "type", "typeof", "until", "uses", "using", "var", "where", "while", "with", "xor"}
        self.spaces = {" ", "\n", "\t", "\0", "\r"}
        self.delimiters = {".", ",", ":", ";", "(", ")", "[", "]", ".."}
        self.operators = {"+", "-", "*", "/", "=", "<", ">", "<>",">=","<=",":=", "+=", "-=", "*=", "/="}
#2.9e-39 <= float(self.buf) <= 1.7e38:
	#-2147483648..2147483647

    def rangeCheckFloat(self,num,state):
        if num>=2.9e-39 and num<=1.7e38:
            return state
        else:
            return 'Range check error'

    def rangeCheckInt(self,num,state):
        if num>=-2147483648 and num<=2147483647:
            return state
        else:
            return 'Range check error'

    def checking_num(self,state,lexeme):
        if 'error' not in state.lower() and lexeme!='':
            if lexeme[0] == '%':
                num=int(lexeme[1:], 2)
                state=self.rangeCheckInt(num,state)
                return num,state
            elif lexeme[0] == '&':
                num=int(lexeme[1:], 8)
                state=self.rangeCheckInt(num,state)
                return num,state
            elif lexeme[0] == '$':
                num=int(lexeme[1:], 16)
                state=self.rangeCheckInt(num,state)
                return num,state
            else:
                return self.checking_float(lexeme,state)
        else:
            return lexeme,state

    def checking_float(self, lexeme,state):
        try: 
            fl_num = float(lexeme)
            if fl_num.is_integer():
                state=self.rangeCheckInt(fl_num,state)
                return int(fl_num),state
            else:
                state=self.rangeCheckFloat(fl_num,state)
                return fl_num,state
        except:
            return '',state

    def IdentCheck(self,lexeme):
        if lexeme in self.key_words:
            return 'Keyword'
        else:
            return 'Identifier'

    def DelimCheck(self,lexeme):
        if lexeme in self.delimiters:
            return 'Delimiter'
        elif lexeme in self.operators:
            return 'Operator'


    def type_getter(self,newstate,state,lexeme):
        if 'err' in newstate.lower():
            return self.types[newstate]
        else:
            try:
                return self.types[state]
            except:
                if self.DelimCheck(lexeme):
                    return self.DelimCheck(lexeme)
                elif self.IdentCheck(lexeme):
                    return self.IdentCheck(lexeme)
                else:
                    return 'Error'