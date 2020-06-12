from sly import Lexer


class BasicLexer(Lexer):
    tokens = {NAME, NUMBER, STRING, IF, THEN,
              ELSE, FOR, FUN, TO, ARROW, EQEQ, PRINT}
    ignore = '\t '

    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';'}

    # Mendefinisikan token
    IF = r'JIKA'
    THEN = r'MAKA'
    ELSE = r'LAINNYA'
    FOR = r'UNTUK'
    FUN = r'FUNGSI'
    TO = r'KE'
    PRINT = r'CETAK'
    ARROW = r'->'
    NAME = r'[A-Za-z_][a-zA-Z0-9_]*'
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
    def newline(self, t):
        self.lineno = t.value.count('\n')
