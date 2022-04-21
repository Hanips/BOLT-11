from sly import Parser

from BoltLexer import BoltLexer

class BoltParser(Parser):
    tokens = BoltLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
    )

    def __init__(self):
        self.env = { }

    @_('')
    def statement(self, p):
        pass

    @_('var_assign')
    def statement(self, p):
        return p.var_assign
    
    @_('NAMA "=" expr')
    def var_assign(self, p):
        return('var_assign', p.NAMA, p.expr)

    @_('NAMA "=" STRING')
    def var_assign(self, p):
        return('var_assign', p.NAMA, p.STRING)
    
    @_('expr')
    def statement(self, p):
        return(p.expr)
    
    @_('expr "+" expr')
    def expr(self, p):
        return ('tambah', p.expr0, p.expr1)

    @_('expr "-" expr')
    def expr(self, p):
        return ('kurang', p.expr0, p.expr1)
    
    @_('expr "/" expr')
    def expr(self, p):
        return ('bagi', p.expr0, p.expr1)
    
    @_('expr "*" expr')
    def expr(self, p):
        return ('kali', p.expr0, p.expr1)
    
    @_('expr "%" expr')
    def expr(self, p):
        return ('mod', p.expr0, p.expr1)

    @_('expr "<" expr')
    def expr(self, p):
        return('less', p.expr0, p.expr1)

    @_('expr ">" expr')
    def expr(self, p):
        return('greater', p.expr0, p.expr1)
    
    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return p.expr
    
    @_('NAMA')
    def expr(self, p):
        return('var', p.NAMA)
    
    @_('ANGKA')
    def expr(self, p):
        return('num', p.ANGKA)

if __name__ == '__main__':
    lexer = BoltLexer()
    parser = BoltParser()
    env = {}
    while True:
        try:
            text = input('bolt-11> ')
        except EOFError:
            print("Program Error")
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree)
