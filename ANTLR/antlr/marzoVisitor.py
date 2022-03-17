# Generated from d:\Programacion\Compiladores\ANTLR\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete generic visitor for a parse tree produced by marzoParser.

class marzoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by marzoParser#program.
    def visitProgram(self, ctx:marzoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#suma.
    def visitSuma(self, ctx:marzoParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#parens.
    def visitParens(self, ctx:marzoParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#var.
    def visitVar(self, ctx:marzoParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#primaria.
    def visitPrimaria(self, ctx:marzoParser.PrimariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#resta.
    def visitResta(self, ctx:marzoParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#declaracion.
    def visitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#asignacion.
    def visitAsignacion(self, ctx:marzoParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#printint.
    def visitPrintint(self, ctx:marzoParser.PrintintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#equals.
    def visitEquals(self, ctx:marzoParser.EqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#less.
    def visitLess(self, ctx:marzoParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#bigg.
    def visitBigg(self, ctx:marzoParser.BiggContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#if.
    def visitIf(self, ctx:marzoParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#ifelse.
    def visitIfelse(self, ctx:marzoParser.IfelseContext):
        return self.visitChildren(ctx)



del marzoParser