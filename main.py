from lexer_tester import lex_test
from parser_tester import parse_test
import sys
import os

import pathlib


dirname = pathlib.Path().absolute()

if sys.argv[1]=='1':
    direname = os.path.join(dirname, 'Tests_lex')
    lex_test(direname)
if sys.argv[1]=='2':
    direname = os.path.join(dirname, 'Tests_parser')
    parse_test(direname)