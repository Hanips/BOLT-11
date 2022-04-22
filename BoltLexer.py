from sly import Lexer

class BoltLexer(Lexer):
    tokens = { CETAK, NAMA, NOMOR, STRING, JIKA, MAKA, KEMUDIAN, UNTUK, FUNG, SAMPAI, PANAH, SAMADENGAN }
    ignore = '\t '
    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';'}

    #Definisi Token
    CETAK = r'cetak'
    NAMA = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    JIKA = r'jika'
    MAKA = r'maka'
    KEMUDIAN = r'kemudian'
    UNTUK = r'loop'
    FUNG = r'fungsi'
    SAMPAI = r'sampai'
    PANAH = r'->'
    SAMADENGAN = r'=='
    
    #Number Token
    @_(r'\d+')
    def NOMOR(self, t):
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
