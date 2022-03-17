# Generated from d:\Programacion\Compiladores\ANTLR\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\6\20N\n\20\r\20\16\20O\3\21\6\21S\n\21\r\21\16\21T\3")
        buf.write("\22\6\22X\n\22\r\22\16\22Y\3\22\3\22\2\2\23\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23\3\2\5\3\2\62;\3\2c|\5\2\13\f\17\17")
        buf.write("\"\"\2_\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2\2\2\t+\3\2\2\2\13")
        buf.write("-\3\2\2\2\r\61\3\2\2\2\17\63\3\2\2\2\219\3\2\2\2\23<\3")
        buf.write("\2\2\2\25>\3\2\2\2\27@\3\2\2\2\31C\3\2\2\2\33E\3\2\2\2")
        buf.write("\35G\3\2\2\2\37M\3\2\2\2!R\3\2\2\2#W\3\2\2\2%&\7-\2\2")
        buf.write("&\4\3\2\2\2\'(\7/\2\2(\6\3\2\2\2)*\7*\2\2*\b\3\2\2\2+")
        buf.write(",\7+\2\2,\n\3\2\2\2-.\7k\2\2./\7p\2\2/\60\7v\2\2\60\f")
        buf.write("\3\2\2\2\61\62\7?\2\2\62\16\3\2\2\2\63\64\7r\2\2\64\65")
        buf.write("\7t\2\2\65\66\7k\2\2\66\67\7p\2\2\678\7v\2\28\20\3\2\2")
        buf.write("\29:\7?\2\2:;\7?\2\2;\22\3\2\2\2<=\7>\2\2=\24\3\2\2\2")
        buf.write(">?\7@\2\2?\26\3\2\2\2@A\7k\2\2AB\7h\2\2B\30\3\2\2\2CD")
        buf.write("\7}\2\2D\32\3\2\2\2EF\7\177\2\2F\34\3\2\2\2GH\7g\2\2H")
        buf.write("I\7n\2\2IJ\7u\2\2JK\7g\2\2K\36\3\2\2\2LN\t\2\2\2ML\3\2")
        buf.write("\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2P \3\2\2\2QS\t\3\2\2")
        buf.write("RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\"\3\2\2\2VX")
        buf.write("\t\4\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2")
        buf.write("\2\2[\\\b\22\2\2\\$\3\2\2\2\6\2OTY\3\b\2\2")
        return buf.getvalue()


class marzoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    Numero = 15
    Variable = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'('", "')'", "'int'", "'='", "'print'", "'=='", 
            "'<'", "'>'", "'if'", "'{'", "'}'", "'else'" ]

    symbolicNames = [ "<INVALID>",
            "Numero", "Variable", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "Numero", "Variable", "WS" ]

    grammarFileName = "marzo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


