from sly import Parser

import BoltLexer

class BoltParser(Parser):
    tokens = BoltLexer.BoltLexer.tokens

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

    @_('UNTUK var_assign SAMPAI expr MAKA statement')
    def statement(self, p):
        return ('untuk_loop', ('untuk_loop_setup', p.var_assign, p.expr), p.statement)

    @_('JIKA condition MAKA statement KEMUDIAN statement')
    def statement(self, p):
        return ('jika_stmt', p.condition, ('branch', p.statement0, p.statement1))

    @_('FUNG NAMA "(" ")" PANAH statement')
    def statement(self, p):
        return ('fung_def', p.NAMA, p.statement)

    @_('NAMA "(" ")"')
    def statement(self, p):
        return ('fung_call', p.NAMA)

    @_('expr SAMADENGAN expr')
    def condition(self, p):
        return ('condition_samadengan', p.expr0, p.expr1)

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
        return ('add', p.expr0, p.expr1)

    @_('expr "-" expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)
    
    @_('expr "/" expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)
    
    @_('expr "*" expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)
    
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
    
    @_('NOMOR')
    def expr(self, p):
        return('num', p.NOMOR)

    @_('CETAK expr')
    def expr(self, p):
        return ('cetak', p.expr)

    @_('CETAK STRING')
    def statement(self, p):
        return ('cetak', p.STRING)

if __name__ == '__main__':
    lexer = BoltLexer.BoltLexer()
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
