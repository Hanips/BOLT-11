from sly import Lexer

class BoltLexer(Lexer):
    tokens = { PRINT, NAME, NUMBER, STRING, IF, THEN, ELSE, FOR, FUNC, TO, ARROW, EQEQ }
    ignore = '\t '
    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';'}

    #Definisi Token
    PRINT = r'cetak'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    IF = r'jika'
    THEN = r'maka'
    ELSE = r'lain'
    FOR = r'loop'
    FUNC = r'fungsi'
    TO = r'sampai'
    ARROW = r'->'
    EQEQ = r'=='
    
    #Number Token
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t
    #Comment Token
    @_(r'#.*')
    def COMMENT(self, t):
        pass
    #Newline Token
    @_(r'\n+')
    def newline(self, t):
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
