# Generated from C:/Users/jemanuel/Documents/ufpi/python-compiler2\trab.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .trabParser import trabParser
else:
    from trabParser import trabParser

# This class defines a complete generic visitor for a parse tree produced by trabParser.

class trabVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by trabParser#prog.
    def visitProg(self, ctx:trabParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#listaDecVars.
    def visitListaDecVars(self, ctx:trabParser.ListaDecVarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#decVars.
    def visitDecVars(self, ctx:trabParser.DecVarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#decParam.
    def visitDecParam(self, ctx:trabParser.DecParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#tipo.
    def visitTipo(self, ctx:trabParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#listaIds.
    def visitListaIds(self, ctx:trabParser.ListaIdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#atrib.
    def visitAtrib(self, ctx:trabParser.AtribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#listaAtribs.
    def visitListaAtribs(self, ctx:trabParser.ListaAtribsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#tipoFunc.
    def visitTipoFunc(self, ctx:trabParser.TipoFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#DecFunc.
    def visitDecFunc(self, ctx:trabParser.DecFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#returnFunc.
    def visitReturnFunc(self, ctx:trabParser.ReturnFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#blocoMain.
    def visitBlocoMain(self, ctx:trabParser.BlocoMainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#stmts.
    def visitStmts(self, ctx:trabParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#stmts_break.
    def visitStmts_break(self, ctx:trabParser.Stmts_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#callFunction.
    def visitCallFunction(self, ctx:trabParser.CallFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#cmdAtrib.
    def visitCmdAtrib(self, ctx:trabParser.CmdAtribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#elseIf.
    def visitElseIf(self, ctx:trabParser.ElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#normalIf.
    def visitNormalIf(self, ctx:trabParser.NormalIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#IfCond.
    def visitIfCond(self, ctx:trabParser.IfCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#IfBreakCond.
    def visitIfBreakCond(self, ctx:trabParser.IfBreakCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#ForCond.
    def visitForCond(self, ctx:trabParser.ForCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#WhileCond.
    def visitWhileCond(self, ctx:trabParser.WhileCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#printExpr.
    def visitPrintExpr(self, ctx:trabParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#printSec.
    def visitPrintSec(self, ctx:trabParser.PrintSecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#printFunc.
    def visitPrintFunc(self, ctx:trabParser.PrintFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#inputFunc.
    def visitInputFunc(self, ctx:trabParser.InputFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#BoolTFExpr.
    def visitBoolTFExpr(self, ctx:trabParser.BoolTFExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#StringExpr.
    def visitStringExpr(self, ctx:trabParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#BoolExpr.
    def visitBoolExpr(self, ctx:trabParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#FloatExpr.
    def visitFloatExpr(self, ctx:trabParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#IdExpr.
    def visitIdExpr(self, ctx:trabParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#CompExpr.
    def visitCompExpr(self, ctx:trabParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#CompAllExpr.
    def visitCompAllExpr(self, ctx:trabParser.CompAllExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#NegateExpr.
    def visitNegateExpr(self, ctx:trabParser.NegateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#AssignExpr.
    def visitAssignExpr(self, ctx:trabParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#IntegerExpr.
    def visitIntegerExpr(self, ctx:trabParser.IntegerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:trabParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#PlusExpr.
    def visitPlusExpr(self, ctx:trabParser.PlusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#ParensExpr.
    def visitParensExpr(self, ctx:trabParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#CallExpr.
    def visitCallExpr(self, ctx:trabParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:trabParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabParser#MinusExpr.
    def visitMinusExpr(self, ctx:trabParser.MinusExprContext):
        return self.visitChildren(ctx)



del trabParser