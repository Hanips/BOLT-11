import BoltExe
import BoltLexer
import BoltParser

from sys import *

lexer = BoltLexer.BoltLexer()
parser = BoltParser.BoltParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    BoltExe.BoltExecute(tree, env)
