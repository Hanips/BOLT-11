import BoltExe
import BoltLexer
import BoltParser

from sys import *

if __name__ == '__main__':
    lexer = BoltLexer.BoltLexer()
    parser = BoltParser.BoltParser()
    print('BOLT-11 Language')
    env = {}
    while True:
        try:
            text = input('bolt-11> ')
        except EOFError:
            print("Error")
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            BoltExe.BoltExecute(tree, env)
