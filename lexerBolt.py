from sly import Lexer

class lexerBolt(Lexer):
    tokens = {NAMA, ANGKA, STRING, JIKA, MAKA, LAIN, UNTUK, FUNC, SAMPAI, SAMADENGAN}
    ignore = '\t '

    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';', '<', '>', '<=', '>=', '%'}

    #Definisi Token
    JIKA = r'JIKA'
    MAKA = r'MAKA'
    LAIN = r'LAIN'
    UNTUK = r'UNTUK'
    FUNC = r'FUNC'
    SAMPAI = r'SAMPAI'
    SAMADENGAN = r'=='
    NAMA = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

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
    lexer = lexerBolt()
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
