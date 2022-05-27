from sly import Lexer

class BoltLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, IF, PRINT, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';', '<', '>' , ':'}

    # pendefinisian token
    IF = r'JIKA'
    PRINT = r'CETAK'
    THEN = r'MAKA'
    ELSE = r'KEMUDIAN'
    FOR = r'UNTUK'
    FUN = r'FUNGSI'
    TO = r'SAMPAI'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')

if __name__ == '__main__':
    lexer = BoltLexer()
    env = {}
    while True:
        try:
            text = input('bolt-11> ')
        except EOFError:
            print("Program Error")
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
