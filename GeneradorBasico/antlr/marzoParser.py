# Generated from d:\Programacion\Compiladores\ANTLR\antlr\marzo.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\2\6\2\23\n\2\r\2\16\2\24\3\2\6\2\30\n")
        buf.write("\2\r\2\16\2\31\3\2\6\2\35\n\2\r\2\16\2\36\5\2!\n\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3*\n\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\7\3\62\n\3\f\3\16\3\65\13\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4>\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5")
        buf.write("\5I\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\5\6[\n\6\3\6\2\3\4\7\2\4\6\b\n\2\2")
        buf.write("\2g\2 \3\2\2\2\4)\3\2\2\2\6=\3\2\2\2\bH\3\2\2\2\nZ\3\2")
        buf.write("\2\2\f\16\5\4\3\2\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2")
        buf.write("\2\17\20\3\2\2\2\20!\3\2\2\2\21\23\5\6\4\2\22\21\3\2\2")
        buf.write("\2\23\24\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25!\3\2\2")
        buf.write("\2\26\30\5\b\5\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2")
        buf.write("\2\2\31\32\3\2\2\2\32!\3\2\2\2\33\35\5\n\6\2\34\33\3\2")
        buf.write("\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37!\3\2")
        buf.write("\2\2 \r\3\2\2\2 \22\3\2\2\2 \27\3\2\2\2 \34\3\2\2\2!\3")
        buf.write("\3\2\2\2\"#\b\3\1\2#$\7\5\2\2$%\5\4\3\2%&\7\6\2\2&*\3")
        buf.write("\2\2\2\'*\7\21\2\2(*\7\22\2\2)\"\3\2\2\2)\'\3\2\2\2)(")
        buf.write("\3\2\2\2*\63\3\2\2\2+,\f\7\2\2,-\7\3\2\2-\62\5\4\3\b.")
        buf.write("/\f\6\2\2/\60\7\4\2\2\60\62\5\4\3\7\61+\3\2\2\2\61.\3")
        buf.write("\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\5")
        buf.write("\3\2\2\2\65\63\3\2\2\2\66\67\7\7\2\2\67>\7\22\2\289\7")
        buf.write("\22\2\29:\7\b\2\2:>\7\21\2\2;<\7\t\2\2<>\7\21\2\2=\66")
        buf.write("\3\2\2\2=8\3\2\2\2=;\3\2\2\2>\7\3\2\2\2?@\7\21\2\2@A\7")
        buf.write("\n\2\2AI\7\21\2\2BC\7\21\2\2CD\7\13\2\2DI\7\21\2\2EF\7")
        buf.write("\21\2\2FG\7\f\2\2GI\7\21\2\2H?\3\2\2\2HB\3\2\2\2HE\3\2")
        buf.write("\2\2I\t\3\2\2\2JK\7\r\2\2KL\5\b\5\2LM\7\16\2\2MN\5\6\4")
        buf.write("\2NO\7\17\2\2O[\3\2\2\2PQ\7\r\2\2QR\5\b\5\2RS\7\16\2\2")
        buf.write("ST\5\6\4\2TU\7\17\2\2UV\7\20\2\2VW\7\16\2\2WX\5\6\4\2")
        buf.write("XY\7\17\2\2Y[\3\2\2\2ZJ\3\2\2\2ZP\3\2\2\2[\13\3\2\2\2")
        buf.write("\r\17\24\31\36 )\61\63=HZ")
        return buf.getvalue()


class marzoParser ( Parser ):

    grammarFileName = "marzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'('", "')'", "'int'", "'='", 
                     "'print'", "'=='", "'<'", "'>'", "'if'", "'{'", "'}'", 
                     "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Numero", "Variable", 
                      "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_statement = 2
    RULE_comparation = 3
    RULE_ifstatement = 4

    ruleNames =  [ "program", "expression", "statement", "comparation", 
                   "ifstatement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    Numero=15
    Variable=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.StatementContext)
            else:
                return self.getTypedRuleContext(marzoParser.StatementContext,i)


        def comparation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ComparationContext)
            else:
                return self.getTypedRuleContext(marzoParser.ComparationContext,i)


        def ifstatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.IfstatementContext)
            else:
                return self.getTypedRuleContext(marzoParser.IfstatementContext,i)


        def getRuleIndex(self):
            return marzoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = marzoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 10
                    self.expression(0)
                    self.state = 13 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << marzoParser.T__2) | (1 << marzoParser.Numero) | (1 << marzoParser.Variable))) != 0)):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 15
                    self.statement()
                    self.state = 18 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << marzoParser.T__4) | (1 << marzoParser.T__6) | (1 << marzoParser.Variable))) != 0)):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 20
                    self.comparation()
                    self.state = 23 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==marzoParser.Numero):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 25
                    self.ifstatement()
                    self.state = 28 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==marzoParser.T__10):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Variable(self):
            return self.getToken(marzoParser.Variable, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class PrimariaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaria" ):
                listener.enterPrimaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaria" ):
                listener.exitPrimaria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaria" ):
                return visitor.visitPrimaria(self)
            else:
                return visitor.visitChildren(self)


    class RestaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResta" ):
                listener.enterResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResta" ):
                listener.exitResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResta" ):
                return visitor.visitResta(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = marzoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [marzoParser.T__2]:
                localctx = marzoParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 33
                self.match(marzoParser.T__2)
                self.state = 34
                self.expression(0)
                self.state = 35
                self.match(marzoParser.T__3)
                pass
            elif token in [marzoParser.Numero]:
                localctx = marzoParser.PrimariaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(marzoParser.Numero)
                pass
            elif token in [marzoParser.Variable]:
                localctx = marzoParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(marzoParser.Variable)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 47
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = marzoParser.SumaContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 41
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 42
                        self.match(marzoParser.T__0)
                        self.state = 43
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = marzoParser.RestaContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 44
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 45
                        self.match(marzoParser.T__1)
                        self.state = 46
                        self.expression(5)
                        pass

             
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignacionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Variable(self):
            return self.getToken(marzoParser.Variable, 0)
        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)


    class DeclaracionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Variable(self):
            return self.getToken(marzoParser.Variable, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)


    class PrintintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintint" ):
                listener.enterPrintint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintint" ):
                listener.exitPrintint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintint" ):
                return visitor.visitPrintint(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = marzoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [marzoParser.T__4]:
                localctx = marzoParser.DeclaracionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(marzoParser.T__4)
                self.state = 53
                self.match(marzoParser.Variable)
                pass
            elif token in [marzoParser.Variable]:
                localctx = marzoParser.AsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(marzoParser.Variable)
                self.state = 55
                self.match(marzoParser.T__5)
                self.state = 56
                self.match(marzoParser.Numero)
                pass
            elif token in [marzoParser.T__6]:
                localctx = marzoParser.PrintintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.match(marzoParser.T__6)
                self.state = 58
                self.match(marzoParser.Numero)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_comparation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EqualsContext(ComparationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ComparationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self, i:int=None):
            if i is None:
                return self.getTokens(marzoParser.Numero)
            else:
                return self.getToken(marzoParser.Numero, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquals" ):
                listener.enterEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquals" ):
                listener.exitEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquals" ):
                return visitor.visitEquals(self)
            else:
                return visitor.visitChildren(self)


    class BiggContext(ComparationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ComparationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self, i:int=None):
            if i is None:
                return self.getTokens(marzoParser.Numero)
            else:
                return self.getToken(marzoParser.Numero, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBigg" ):
                listener.enterBigg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBigg" ):
                listener.exitBigg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBigg" ):
                return visitor.visitBigg(self)
            else:
                return visitor.visitChildren(self)


    class LessContext(ComparationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ComparationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self, i:int=None):
            if i is None:
                return self.getTokens(marzoParser.Numero)
            else:
                return self.getToken(marzoParser.Numero, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLess" ):
                listener.enterLess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLess" ):
                listener.exitLess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess" ):
                return visitor.visitLess(self)
            else:
                return visitor.visitChildren(self)



    def comparation(self):

        localctx = marzoParser.ComparationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comparation)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = marzoParser.EqualsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(marzoParser.Numero)
                self.state = 62
                self.match(marzoParser.T__7)
                self.state = 63
                self.match(marzoParser.Numero)
                pass

            elif la_ == 2:
                localctx = marzoParser.LessContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(marzoParser.Numero)
                self.state = 65
                self.match(marzoParser.T__8)
                self.state = 66
                self.match(marzoParser.Numero)
                pass

            elif la_ == 3:
                localctx = marzoParser.BiggContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.match(marzoParser.Numero)
                self.state = 68
                self.match(marzoParser.T__9)
                self.state = 69
                self.match(marzoParser.Numero)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_ifstatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfContext(IfstatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.IfstatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparation(self):
            return self.getTypedRuleContext(marzoParser.ComparationContext,0)

        def statement(self):
            return self.getTypedRuleContext(marzoParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class IfelseContext(IfstatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.IfstatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparation(self):
            return self.getTypedRuleContext(marzoParser.ComparationContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.StatementContext)
            else:
                return self.getTypedRuleContext(marzoParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfelse" ):
                listener.enterIfelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfelse" ):
                listener.exitIfelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse" ):
                return visitor.visitIfelse(self)
            else:
                return visitor.visitChildren(self)



    def ifstatement(self):

        localctx = marzoParser.IfstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifstatement)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = marzoParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(marzoParser.T__10)
                self.state = 73
                self.comparation()
                self.state = 74
                self.match(marzoParser.T__11)
                self.state = 75
                self.statement()
                self.state = 76
                self.match(marzoParser.T__12)
                pass

            elif la_ == 2:
                localctx = marzoParser.IfelseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(marzoParser.T__10)
                self.state = 79
                self.comparation()
                self.state = 80
                self.match(marzoParser.T__11)
                self.state = 81
                self.statement()
                self.state = 82
                self.match(marzoParser.T__12)
                self.state = 83
                self.match(marzoParser.T__13)
                self.state = 84
                self.match(marzoParser.T__11)
                self.state = 85
                self.statement()
                self.state = 86
                self.match(marzoParser.T__12)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




