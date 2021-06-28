from lexer_tester import lex_test
from parser_tester import parse_test


test_type=int(input('1 — Тестирование лексера\n2 — тестирование парсера\n'))
    
if test_type==1:
    lex_test('C:/Users/krisl/Desktop/Компилятор/Tests_lex')
if test_type==2:
    parse_test('C:/Users/krisl/Desktop/Компилятор/Tests_parser')