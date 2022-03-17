from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser


class Gencode(marzoListener):
    def __init__(self):
        self.r = 0
        self.stack = []

    def enterProgram(self, ctx: marzoParser.ProgramContext):
        print("enter")

    def exitPrimaria(self, ctx: marzoParser.PrimariaContext):
        self.stack.append(self.r)
        print("lw $t" + str(self.r) + ", " + ctx.Numero().getText())
        self.r += 1

    def exitVar(self, ctx: marzoParser.VarContext):
        self.stack.append(self.r)
        print("lw $t" + str(self.r) + ", " + ctx.Variable().getText())
        self.r += 1

    def exitSuma(self, ctx: marzoParser.SumaContext):
        print("add $t" + str((self.r)) + ", " + "$t" +
              str(self.stack.pop()) + ", " + "$t" + str(self.stack.pop()))
        self.stack.append(self.r)

    def exitResta(self, ctx: marzoParser.RestaContext):
        print("sub $t" + str((self.r)) + ", " + "$t" + 
                str(self.stack.pop()) + ", " + "$t" + str(self.stack.pop()))
        self.stack.append(self.r)

    def exitAsignacion(self, ctx: marzoParser.AsignacionContext):
        print("lw $t" + str(self.r) + ", " + ctx.Numero().getText())

    def exitDeclaracion(self, ctx: marzoParser.DeclaracionContext):
        self.stack.append(self.r)
        print("sw $t" + str(self.r) + ", " + ctx.Variable().getText())
        self.r += 1
    
    def exitPrintint(self, ctx: marzoParser.PrintintContext):
        print("li $t" + str(self.r) + ", " + "1")
        print("lw $a" + str(self.r) + ", " + ctx.Numero().getText())
        print("syscall")

    #missing    
    def exitLess(self, ctx: marzoParser.LessContext):
        print("slt")
    #missing
    def exitBigg(self, ctx: marzoParser.BiggContext):
        print("bgt")
    #missing
    def exitEquals(self, ctx: marzoParser.EqualsContext):
        print("beq")
    #missing
    def exitIf(self, ctx: marzoParser.IfContext):
        print("if")
    #missing
    def exitIfelse(self, ctx: marzoParser.IfelseContext):
        print("ifelse")

