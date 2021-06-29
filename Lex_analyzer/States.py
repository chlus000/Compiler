from string import ascii_letters
class State(object):

    def __init__(self):
        self.States={'S':{"'":'StrStart','"':'F','Ident':'Ident','Int':'Int','_':'Ident','+':'Delim','-':'Delim','*':'Delim',':':'Delim',';':'Delim',',':'Delim','.':'DoublePoint','>':'Delim','<':'Delim',
                        '=':'Delim','[':'Delim',']':'Delim','^':'Delim','@':'ErrSynt','/':'Slash','{':'ManyCom{','}':'ErrSynt','(':'OpBracket',')':'Delim',' ':'S', '\n':'S', '\t':'S','\0':'S', '\r':'S','':'F','?':'D', '%':'Int2','&': 'Int8','$': 'Int16','#':'Cont'},
                    'Ident':{'"':'F',"'":'ErrSynt','Ident':'Ident','Int':'Ident','_':'Ident','+':'F','-':'F','*':'F',':':'F',';':'F',',':'F','.':'F','>':'F','<':'F',
                            '=':'F','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F', '':'F'},
                    'StrStart':{"'":'StrEnd','"':'F','Str':'Str','Int':'Str','_':'Str','+':'Str','-':'Str','*':'Str',':':'Str',';':'Str',',':'Str','.':'Str','>':'Str','<':'Str',
                                '=':'Str','[':'Str',']':'Str','^':'Str','@':'Str','/':'Str','{':'Str','}':'Str','(':'Str',')':'F',' ':'Str', '\n':'ErrStr', '\t':'Str','':'ErrStr','\\':'Str','%':'Str','&': 'Str','$': 'Str'},
                    'Str':{"'":'StrEnd','"':'F','Str':'Str','Int':'Str','_':'Str','+':'Str','-':'Str','*':'Str',':':'Str',';':'Str',',':'Str','.':'Str','>':'Str','<':'Str',
                            '=':'Str','[':'Str',']':'Str','^':'Str','@':'Str','/':'Str','{':'Str','}':'Str','(':'Str',')':'F',' ':'Str', '\n':'ErrStr', '\t':'Str','':'ErrStr','\\':'Str'},
                    'StrEnd':{"'":'F','"':'F','Str':'F','Int':'F','_':'F','+':'F','-':'F','*':'F',':':'F',';':'F',',':'F','.':'F','>':'F','<':'F',
                            '=':'F','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F','':'F','#':'Cont'},
                    'Cont':{"'":'ErrStrCont','"':'ErrStrCont','Str':'ErrStrCont','Int':'IntStr','_':'ErrStrCont','+':'ErrStrCont','-':'ErrStrCont','*':'ErrStrCont',':':'ErrStrCont',';':'ErrStrCont',',':'ErrStrCont','.':'ErrStrCont','>':'ErrStrCont','<':'ErrStrCont',
                            '=':'ErrStrCont','[':'ErrStrCont',']':'ErrStrCont','^':'ErrStrCont','@':'ErrStrCont','/':'ErrStrCont','{':'ErrStrCont','}':'ErrStrCont','(':'ErrStrCont',')':'ErrStrCont',' ':'ErrStrCont', '\n':'ErrStrCont', '\t':'ErrStrCont','':'ErrStrCont','#':'ErrStrCont'},
                    'IntStr':{"'":'StrStart','"':'ErrStr','Str':'ErrStr','Int':'IntStr','_':'F','+':'F','-':'F','*':'F',':':'F',';':'F',',':'F','.':'F','F':'F','<':'F',
                            '=':'F','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F','':'F','#':'Cont'},
                    'Int':{"'":'ErrSynt','"':'F','e':'RealE','E':'RealE','Ident':'ErrSynt','Int':'Int','_':'ErrSynt','+':'F','-':'F','*':'F',':':'F',';':'F',',':'F','.':'Point','>':'F','<':'F',
                            '=':'F','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F', '':'F'},
                    'Point':{"'":'ErrSynt','"':'F','Ident':'ErrSynt','Int':'Real','_':'ErrSynt','+':'F','-':'F','*':'F',':':'F',';':'F',',':'F','.':'DoublePoint','>':'F','<':'F',
                            '=':'F','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F', '':'F'},
                    'DoublePoint':{'':'F','.':'DoublePointEnd','\n':'F','Ident':'F','Int':'F'},
                    'DoublePointEnd':{'':'F','.':'F','\n':'F','Ident':'F','Int':'F'},
                    'Int2':{"'":'F','"':'F','Ident':'F','Int':'Int2','_':'F','+':'F','-':'F','*':'F',':':'F',';':'F',',':'F','.':'F','>':'F','<':'F',
                        '=':'F','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F', '':'F'},
                    'Int8':{"'":'F','"':'F','Ident':'F','Int':'Int8','_':'F','+':'F','-':'F','*':'F',':':'F',';':'F',',':'F','.':'F','>':'F','<':'F',
                        '=':'F','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F', '':'F'},
                    'Int16':{"'":'F','"':'F','Ident':'Int16','Int':'Int16','_':'F','+':'F','-':'F','*':'F',':':'F',';':'F',',':'F','.':'F','>':'F','<':'F',
                        '=':'F','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F', '':'F'},
                    'Delim':{"'":'F','"':'F','Ident':'F','Int':'F','_':'F','+':'F','-':'F','*':'F',':':'Delim',';':'F',',':'Delim','.':'Delim','>':'Delim','<':'Delim',
                        '=':'Delim','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F', '':'F'},
                    'Slash':{"'":'F','"':'F','Ident':'F','Int':'F','_':'F','+':'F','-':'F','*':'F',':':'F',';':'ErrSynt',',':'ErrSynt','.':'ErrSynt','>':'F','<':'F',
                        '=':'F','[':'F',']':'F','^':'F','@':'F','/':'OneCom','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F', '':'F'},
                    'OneCom':{"'":'OneCom','"':'OneCom','Ident':'OneCom','Int':'OneCom','_':'OneCom','+':'OneCom','-':'OneCom','*':'OneCom',':':'OneCom',';':'OneCom',',':'OneCom',
                    '.':'OneCom','>':'OneCom','<':'OneCom','=':'OneCom','[':'OneCom',']':'OneCom','^':'OneCom','@':'OneCom','/':'OneCom','{':'OneCom','}':'OneCom','(':'OneCom',
                    ')':'OneCom',' ':'OneCom', '\n':'S', '\t':'OneCom', '':'S','\\':'OneCom','%':'OneCom','&': 'OneCom','$': 'OneCom'},
                    'ManyCom{':{"'":'ManyCom{','"':'F','Ident':'ManyCom{','Int':'ManyCom{','_':'ManyCom{','+':'ManyCom{','-':'ManyCom{','*':'ManyCom{',':':'ManyCom{',';':'ManyCom{',
                                ',':'ManyCom{','.':'ManyCom{','>':'ManyCom{','<':'ManyCom{', '=':'ManyCom{','[':'ManyCom{',']':'ManyCom{','^':'ManyCom{','@':'ManyCom{','/':'ManyCom{',
                                '{':'ManyCom{','}':'ManyCom}','(':'ManyCom{',')':'F',' ':'ManyCom{', '\n':'ManyCom{', '\t':'ManyCom{','':'ErrSynt','\\':'ManyCom{','%':'ManyCom{','&': 'ManyCom{','$': 'ManyCom{'},
                    'ManyCom}':{'':'S','\n':'S'},
                    'OpBracket':{"'":'F','"':'F','Ident':'F','Int':'F','_':'F','+':'F','-':'F','*':'ManyCom(*',':':'F',';':'F',',':'F','.':'F','>':'F','<':'F',
                        '=':'F','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F', '':'F'},
                    'ManyCom(*':{"'":'ManyCom(*','"':'F','Ident':'ManyCom(*','Int':'ManyCom(*','_':'ManyCom(*','+':'ManyCom(*','-':'ManyCom(*','*':'Close*',':':'ManyCom(*',';':'ManyCom(*',
                                ',':'ManyCom(*','.':'ManyCom(*','>':'ManyCom(*','<':'ManyCom(*', '=':'ManyCom(*','[':'ManyCom(*',']':'ManyCom(*','^':'ManyCom(*','@':'ManyCom(*','/':'ManyCom(*',
                                '{':'ManyCom(*','}':'ManyCom(*','(':'ManyCom(*',')':'F',' ':'ManyCom(*', '\n':'ManyCom(*', '\t':'ManyCom(*','':'ErrSynt','\\':'ManyCom(*','%':'ManyCom(*','&': 'ManyCom(*','$': 'ManyCom(*'},
                    'Close*':{"'":'ManyCom(*','"':'F','Ident':'ManyCom(*','Int':'ManyCom(*','_':'ManyCom(*','+':'ManyCom(*','-':'ManyCom(*','*':'Close*',':':'ManyCom(*',';':'ManyCom(*',
                                ',':'ManyCom(*','.':'ManyCom(*','>':'ManyCom(*','<':'ManyCom(*', '=':'ManyCom(*','[':'ManyCom(*',']':'ManyCom(*','^':'ManyCom(*','@':'ManyCom(*','/':'ManyCom(*',
                                '{':'ManyCom(*','}':'ManyCom(*','(':'ManyCom(*',')':'ManyCom*)',' ':'ManyCom(*', '\n':'ManyCom(*', '\t':'ManyCom(*','':'ErrSynt','\\':'ManyCom(*'},
                    'ManyCom*)':{'':'S','\n':'S'},
                    'Real':{"'":'ErrSynt','"':'F','e':'RealE','E':'RealE','Ident':'ErrSynt','Int':'Real','_':'ErrSynt','+':'F','-':'F','*':'F',':':'F',';':'F',',':'F','.':'Point','>':'F','<':'F',
                        '=':'F','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F', '':'F'},
                    'RealE':{"'":'ErrSynt','"':'F','Ident':'ErrSynt','Int':'RealE','_':'ErrSynt','+':'ReadlEOp','-':'ReadlEOp','*':'F',':':'F',';':'F',',':'F','.':'ErrSynt','>':'F','<':'F',
                        '=':'F','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F', '':'ErrSynt'},
                    'ReadlEOp':{'Int':'RealNum'},
                    'RealNum':{"'":'F','"':'F','Ident':'ErrSynt','Int':'RealNum','_':'F','+':'F','-':'F','*':'F',':':'F',';':'F',',':'F','.':'ErrSynt','>':'F','<':'F',
                        '=':'F','[':'F',']':'F','^':'F','@':'F','/':'F','{':'F','}':'F','(':'F',')':'F',' ':'F', '\n':'F', '\t':'F', '':'F'}}
        
        


    def LetterNumCheck(self,ch,state):
        if ch=='':
            return ch
        if ((state=='Int' or state=='Real') and (ch=='e' or ch=='E')):
            return ch
        if state=='Int16':
            if ch in 'ABCDEFabcdef':
                return 'Ident'
        if state=='Int8':
            if ch in '01234567':
                return 'Int'
        if state=='Int2':
            if ch in '01':
                return 'Int'
        if (ch in ascii_letters) and state!='Int16':
            if state=='Str' or state=='StrStart' or state=='StrEnd':
                return 'Str'
            else:
                return 'Ident'
        if ch.isalpha():
            if state=='Str' or state=='StrStart':
                return 'Str'
            elif state=='OneCom' or state=='ManyCom{' or state=='ManyCom(*':
                return 'Ident'
        elif ch.isdigit():
            return 'Int'
        else:
            return ch
        
    def GetNextState(self,ch,state):
        try:
            newch=self.LetterNumCheck(ch,state)
            return self.States[state][newch]
        except:
            if ch.isalpha():
                return 'ErrSynt'

            
