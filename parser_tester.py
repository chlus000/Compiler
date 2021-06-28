import os
from Parser.Expr import ExprParser

class parse_test:
    def __init__(self,tests):
	    self.test(tests)

    def test(self,tests):
        c=0
        for file in os.listdir(tests):
            test_checker=True
            if 'ans' not in file:
                check = ExprParser(os.path.join(tests,file)).ParseExpr().Print(0).strip()
                res = open(os.path.join(tests, os.path.splitext(file)[0]+' ans.txt'), "r", encoding="utf-8")
                try:                    
                    corr = res.read().strip()
                    if check!=corr:
                        print(check)
                        print(corr)
                        print('Ошибка на тесте №'+file)
                        test_checker=False
                            #break
                    if test_checker:
                        print('Тест #'+os.path.splitext(file)[0]+' +')
                        c+=1
                except: 
                    pass
        print('Всего верных тестов:',c)