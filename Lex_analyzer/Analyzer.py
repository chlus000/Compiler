class Analyzer:
    def __init__(self):
        self.types={'Err':'Error',
                    'S':'',
                    'StrEnd':'String',
                    'Int':'Integer',
                    'Point':'Delimiter',
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

    def checking_num(self,state,lexeme):
        if state!='Error' and lexeme!='':
            if lexeme[0] == '%':
                return int(lexeme[1:], 2)
            elif lexeme[0] == '&':
                return int(lexeme[1:], 8)
            elif lexeme[0] == '$':
                return int(lexeme[1:], 16)
            else:
                return self.checking_float(lexeme)

    def checking_float(self, lexeme):
        try: 
            fl_num = float(lexeme)
            if fl_num.is_integer():
                return int(fl_num)
            else:
                return fl_num
        except:
            return ''

    def IdentCheck(self,lexeme):
        if lexeme in self.key_words:
            return 'Key word'
        else:
            return 'Identifier'

    def DelimCheck(self,lexeme):
        if lexeme in self.delimiters:
            return 'Delimiter'
        elif lexeme in self.operators:
            return 'Operator'


    def type_getter(self,newstate,state,lexeme):
        if newstate=='Err':
            return 'Error'
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