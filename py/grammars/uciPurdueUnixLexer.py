# Generated from grammars/uciPurdueUnix.g4 by ANTLR 4.5.1
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\r")
        buf.write("H\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\6\4\37\n\4\r\4\16\4 \3\5\3\5\3\6\6\6&\n\6\r\6")
        buf.write("\16\6\'\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\f\7\fD\n\f\f\f\16\fG\13\f\2\2\r\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\3\2\5\3\2\62;\3\2")
        buf.write("C|\4\2\13\13\"\"J\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3")
        buf.write("\2\2\2\5\33\3\2\2\2\7\36\3\2\2\2\t\"\3\2\2\2\13%\3\2\2")
        buf.write("\2\r)\3\2\2\2\17-\3\2\2\2\21\65\3\2\2\2\23=\3\2\2\2\25")
        buf.write("?\3\2\2\2\27E\3\2\2\2\31\32\7>\2\2\32\4\3\2\2\2\33\34")
        buf.write("\7@\2\2\34\6\3\2\2\2\35\37\t\2\2\2\36\35\3\2\2\2\37 \3")
        buf.write("\2\2\2 \36\3\2\2\2 !\3\2\2\2!\b\3\2\2\2\"#\t\3\2\2#\n")
        buf.write("\3\2\2\2$&\5\t\5\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(")
        buf.write("\3\2\2\2(\f\3\2\2\2)*\t\4\2\2*+\3\2\2\2+,\b\7\2\2,\16")
        buf.write("\3\2\2\2-.\7,\2\2./\7,\2\2/\60\7U\2\2\60\61\7Q\2\2\61")
        buf.write("\62\7H\2\2\62\63\7,\2\2\63\64\7,\2\2\64\20\3\2\2\2\65")
        buf.write("\66\7,\2\2\66\67\7,\2\2\678\7G\2\289\7Q\2\29:\7H\2\2:")
        buf.write(";\7,\2\2;<\7,\2\2<\22\3\2\2\2=>\7~\2\2>\24\3\2\2\2?@\7")
        buf.write("/\2\2@A\5\t\5\2A\26\3\2\2\2BD\5\25\13\2CB\3\2\2\2DG\3")
        buf.write("\2\2\2EC\3\2\2\2EF\3\2\2\2F\30\3\2\2\2GE\3\2\2\2\6\2 ")
        buf.write("\'E\3\b\2\2")
        return buf.getvalue()


class uciPurdueUnixLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    NUMBER = 3
    TEXT = 4
    WORD = 5
    WHITESPACE = 6
    SESS_START = 7
    SESS_END = 8
    PIPE = 9
    OPTION = 10
    OPTIONS = 11

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'**SOF**'", "'**EOF**'", "'|'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "TEXT", "WORD", "WHITESPACE", "SESS_START", "SESS_END", 
            "PIPE", "OPTION", "OPTIONS" ]

    ruleNames = [ "T__0", "T__1", "NUMBER", "TEXT", "WORD", "WHITESPACE", 
                  "SESS_START", "SESS_END", "PIPE", "OPTION", "OPTIONS" ]

    grammarFileName = "uciPurdueUnix.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


