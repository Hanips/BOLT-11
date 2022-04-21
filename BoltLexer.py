from sly import Lexer

class BoltLexer(Lexer):
    tokens = {NAMA, ANGKA, STRING, JIKA, MAKA, LAIN, UNTUK, FUNG, SAMPAI, SAMADENGAN}
    ignore = '\t '
    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';', '<', '>', '<=', '>=', '%'}

    #Definisi Token
    NAMA = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    JIKA = r'JIKA'
    MAKA = r'MAKA'
    LAIN = r'LAIN'
    UNTUK = r'UNTUK'
    FUNG = r'FUNG'
    SAMPAI = r'SAMPAI'
    SAMADENGAN = r'=='
    
    #Number Token
    @_(r'\d+')
    def ANGKA(self, t):
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