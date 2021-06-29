from Lex_analyzer.Lexer import Lexer
import os

class lex_test:
    def __init__(self,tests):
	    self.test(tests)

    def test(self,tests):
        c=0
        for file in os.listdir(tests):
            
            test_checker=True
            if 'ans' not in file and 'res' not in file:
                
                check = Lexer(os.path.join(tests,file))
                f=open(os.path.join(tests, os.path.splitext(file)[0]+' res.txt'),'w', encoding='utf-8')
                self.lexeme = check.NewLex()
                while self.lexeme.lexeme:
                    f.write(self.lexeme_out()+'\n')
                    if self.lexeme.error:
                        break
                    self.lexeme = check.NewLex()
                    
                f.close()

                ans=open(os.path.join(tests, os.path.splitext(file)[0]+' ans.txt'),'r', encoding='utf-8')
                f=open(os.path.join(tests, os.path.splitext(file)[0]+' res.txt'),'r', encoding='utf-8')
                while True:
                    corr=ans.readline().strip()
                    res=f.readline().strip()
                    if corr!=res:
                        print(res)
                        print(corr)
                        print(f'Ошибка на тесте № {file}')
                        test_checker=False
                        break
                    if res=='':
                        break
                if test_checker:
                    print(f'Тест # {os.path.splitext(file)[0]} +')
                    c+=1

        print(f'Всего верных тестов: {c}')

    def lexeme_out(self):
        if self.lexeme.error:
            return f"{self.lexeme.line} {self.lexeme.position} {self.lexeme.type} {self.lexeme.lexeme}"
        else:
            return f"{self.lexeme.line} {self.lexeme.position} {self.lexeme.type} {self.lexeme.lexeme} {self.lexeme.num}"