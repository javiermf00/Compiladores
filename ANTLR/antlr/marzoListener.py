# Generated from d:\Programacion\Compiladores\ANTLR\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete listener for a parse tree produced by marzoParser.
class marzoListener(ParseTreeListener):

    # Enter a parse tree produced by marzoParser#program.
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        pass

    # Exit a parse tree produced by marzoParser#program.
    def exitProgram(self, ctx:marzoParser.ProgramContext):
        pass


    # Enter a parse tree produced by marzoParser#suma.
    def enterSuma(self, ctx:marzoParser.SumaContext):
        pass

    # Exit a parse tree produced by marzoParser#suma.
    def exitSuma(self, ctx:marzoParser.SumaContext):
        pass


    # Enter a parse tree produced by marzoParser#parens.
    def enterParens(self, ctx:marzoParser.ParensContext):
        pass

    # Exit a parse tree produced by marzoParser#parens.
    def exitParens(self, ctx:marzoParser.ParensContext):
        pass


    # Enter a parse tree produced by marzoParser#var.
    def enterVar(self, ctx:marzoParser.VarContext):
        pass

    # Exit a parse tree produced by marzoParser#var.
    def exitVar(self, ctx:marzoParser.VarContext):
        pass


    # Enter a parse tree produced by marzoParser#primaria.
    def enterPrimaria(self, ctx:marzoParser.PrimariaContext):
        pass

    # Exit a parse tree produced by marzoParser#primaria.
    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        pass


    # Enter a parse tree produced by marzoParser#resta.
    def enterResta(self, ctx:marzoParser.RestaContext):
        pass

    # Exit a parse tree produced by marzoParser#resta.
    def exitResta(self, ctx:marzoParser.RestaContext):
        pass


    # Enter a parse tree produced by marzoParser#declaracion.
    def enterDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by marzoParser#declaracion.
    def exitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by marzoParser#asignacion.
    def enterAsignacion(self, ctx:marzoParser.AsignacionContext):
        pass

    # Exit a parse tree produced by marzoParser#asignacion.
    def exitAsignacion(self, ctx:marzoParser.AsignacionContext):
        pass


    # Enter a parse tree produced by marzoParser#printint.
    def enterPrintint(self, ctx:marzoParser.PrintintContext):
        pass

    # Exit a parse tree produced by marzoParser#printint.
    def exitPrintint(self, ctx:marzoParser.PrintintContext):
        pass


    # Enter a parse tree produced by marzoParser#equals.
    def enterEquals(self, ctx:marzoParser.EqualsContext):
        pass

    # Exit a parse tree produced by marzoParser#equals.
    def exitEquals(self, ctx:marzoParser.EqualsContext):
        pass


    # Enter a parse tree produced by marzoParser#less.
    def enterLess(self, ctx:marzoParser.LessContext):
        pass

    # Exit a parse tree produced by marzoParser#less.
    def exitLess(self, ctx:marzoParser.LessContext):
        pass


    # Enter a parse tree produced by marzoParser#bigg.
    def enterBigg(self, ctx:marzoParser.BiggContext):
        pass

    # Exit a parse tree produced by marzoParser#bigg.
    def exitBigg(self, ctx:marzoParser.BiggContext):
        pass


    # Enter a parse tree produced by marzoParser#if.
    def enterIf(self, ctx:marzoParser.IfContext):
        pass

    # Exit a parse tree produced by marzoParser#if.
    def exitIf(self, ctx:marzoParser.IfContext):
        pass


    # Enter a parse tree produced by marzoParser#ifelse.
    def enterIfelse(self, ctx:marzoParser.IfelseContext):
        pass

    # Exit a parse tree produced by marzoParser#ifelse.
    def exitIfelse(self, ctx:marzoParser.IfelseContext):
        pass



del marzoParser