from Lex_analyzer.Lexer import Lexer
import os

class lex_test:
    def __init__(self,tests):
	    self.test(tests)

    def test(self,tests):
        c=0
        for file in os.listdir(tests):
            test_checker=True
            if 'ans' not in file:
                check = Lexer(os.path.join(tests,file))
                res = open(os.path.join(tests, os.path.splitext(file)[0]+' ans.txt'), "r", encoding="utf-8")
                try:                    
                    for line in res:
                        self.lexeme = check.NewLex()
                        lex=self.lexeme_out().strip()
                        corr = line.replace("\n", "").strip()
                        if lex!=corr:
                            print(lex)
                            print(corr)
                            print('Ошибка на тесте №'+file)
                            test_checker=False
                            break
                    if test_checker:
                        print('Тест #'+os.path.splitext(file)[0]+' +')
                        c+=1
                except: 
                    pass
        print('Всего верных тестов:',c)

    def lexeme_out(self):
        if self.lexeme.lexeme=='':
            return ''
        elif self.lexeme.error:
            return str(self.lexeme.line)+' '+str(self.lexeme.position)+' ' +str(self.lexeme.type)+' '+str(self.lexeme.lexeme)
        else:
            return str(self.lexeme.line)+' '+str(self.lexeme.position)+' '+str(self.lexeme.type)+' ' +str(self.lexeme.lexeme)+ ' '+str(self.lexeme.num)