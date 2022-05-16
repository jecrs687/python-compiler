# Generated from C:/Users/jemanuel/Documents/ufpi/python-compiler2\trab.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .trabParser import trabParser
else:
    from trabParser import trabParser

# This class defines a complete listener for a parse tree produced by trabParser.
class trabListener(ParseTreeListener):

    # Enter a parse tree produced by trabParser#prog.
    def enterProg(self, ctx:trabParser.ProgContext):
        pass

    # Exit a parse tree produced by trabParser#prog.
    def exitProg(self, ctx:trabParser.ProgContext):
        pass


    # Enter a parse tree produced by trabParser#listaDecVars.
    def enterListaDecVars(self, ctx:trabParser.ListaDecVarsContext):
        pass

    # Exit a parse tree produced by trabParser#listaDecVars.
    def exitListaDecVars(self, ctx:trabParser.ListaDecVarsContext):
        pass


    # Enter a parse tree produced by trabParser#decVars.
    def enterDecVars(self, ctx:trabParser.DecVarsContext):
        pass

    # Exit a parse tree produced by trabParser#decVars.
    def exitDecVars(self, ctx:trabParser.DecVarsContext):
        pass


    # Enter a parse tree produced by trabParser#decParam.
    def enterDecParam(self, ctx:trabParser.DecParamContext):
        pass

    # Exit a parse tree produced by trabParser#decParam.
    def exitDecParam(self, ctx:trabParser.DecParamContext):
        pass


    # Enter a parse tree produced by trabParser#tipo.
    def enterTipo(self, ctx:trabParser.TipoContext):
        pass

    # Exit a parse tree produced by trabParser#tipo.
    def exitTipo(self, ctx:trabParser.TipoContext):
        pass


    # Enter a parse tree produced by trabParser#listaIds.
    def enterListaIds(self, ctx:trabParser.ListaIdsContext):
        pass

    # Exit a parse tree produced by trabParser#listaIds.
    def exitListaIds(self, ctx:trabParser.ListaIdsContext):
        pass


    # Enter a parse tree produced by trabParser#atrib.
    def enterAtrib(self, ctx:trabParser.AtribContext):
        pass

    # Exit a parse tree produced by trabParser#atrib.
    def exitAtrib(self, ctx:trabParser.AtribContext):
        pass


    # Enter a parse tree produced by trabParser#listaAtribs.
    def enterListaAtribs(self, ctx:trabParser.ListaAtribsContext):
        pass

    # Exit a parse tree produced by trabParser#listaAtribs.
    def exitListaAtribs(self, ctx:trabParser.ListaAtribsContext):
        pass


    # Enter a parse tree produced by trabParser#tipoFunc.
    def enterTipoFunc(self, ctx:trabParser.TipoFuncContext):
        pass

    # Exit a parse tree produced by trabParser#tipoFunc.
    def exitTipoFunc(self, ctx:trabParser.TipoFuncContext):
        pass


    # Enter a parse tree produced by trabParser#DecFunc.
    def enterDecFunc(self, ctx:trabParser.DecFuncContext):
        pass

    # Exit a parse tree produced by trabParser#DecFunc.
    def exitDecFunc(self, ctx:trabParser.DecFuncContext):
        pass


    # Enter a parse tree produced by trabParser#returnFunc.
    def enterReturnFunc(self, ctx:trabParser.ReturnFuncContext):
        pass

    # Exit a parse tree produced by trabParser#returnFunc.
    def exitReturnFunc(self, ctx:trabParser.ReturnFuncContext):
        pass


    # Enter a parse tree produced by trabParser#blocoMain.
    def enterBlocoMain(self, ctx:trabParser.BlocoMainContext):
        pass

    # Exit a parse tree produced by trabParser#blocoMain.
    def exitBlocoMain(self, ctx:trabParser.BlocoMainContext):
        pass


    # Enter a parse tree produced by trabParser#stmts.
    def enterStmts(self, ctx:trabParser.StmtsContext):
        pass

    # Exit a parse tree produced by trabParser#stmts.
    def exitStmts(self, ctx:trabParser.StmtsContext):
        pass


    # Enter a parse tree produced by trabParser#stmts_break.
    def enterStmts_break(self, ctx:trabParser.Stmts_breakContext):
        pass

    # Exit a parse tree produced by trabParser#stmts_break.
    def exitStmts_break(self, ctx:trabParser.Stmts_breakContext):
        pass


    # Enter a parse tree produced by trabParser#callFunction.
    def enterCallFunction(self, ctx:trabParser.CallFunctionContext):
        pass

    # Exit a parse tree produced by trabParser#callFunction.
    def exitCallFunction(self, ctx:trabParser.CallFunctionContext):
        pass


    # Enter a parse tree produced by trabParser#cmdAtrib.
    def enterCmdAtrib(self, ctx:trabParser.CmdAtribContext):
        pass

    # Exit a parse tree produced by trabParser#cmdAtrib.
    def exitCmdAtrib(self, ctx:trabParser.CmdAtribContext):
        pass


    # Enter a parse tree produced by trabParser#elseIf.
    def enterElseIf(self, ctx:trabParser.ElseIfContext):
        pass

    # Exit a parse tree produced by trabParser#elseIf.
    def exitElseIf(self, ctx:trabParser.ElseIfContext):
        pass


    # Enter a parse tree produced by trabParser#normalIf.
    def enterNormalIf(self, ctx:trabParser.NormalIfContext):
        pass

    # Exit a parse tree produced by trabParser#normalIf.
    def exitNormalIf(self, ctx:trabParser.NormalIfContext):
        pass


    # Enter a parse tree produced by trabParser#IfCond.
    def enterIfCond(self, ctx:trabParser.IfCondContext):
        pass

    # Exit a parse tree produced by trabParser#IfCond.
    def exitIfCond(self, ctx:trabParser.IfCondContext):
        pass


    # Enter a parse tree produced by trabParser#IfBreakCond.
    def enterIfBreakCond(self, ctx:trabParser.IfBreakCondContext):
        pass

    # Exit a parse tree produced by trabParser#IfBreakCond.
    def exitIfBreakCond(self, ctx:trabParser.IfBreakCondContext):
        pass


    # Enter a parse tree produced by trabParser#ForCond.
    def enterForCond(self, ctx:trabParser.ForCondContext):
        pass

    # Exit a parse tree produced by trabParser#ForCond.
    def exitForCond(self, ctx:trabParser.ForCondContext):
        pass


    # Enter a parse tree produced by trabParser#WhileCond.
    def enterWhileCond(self, ctx:trabParser.WhileCondContext):
        pass

    # Exit a parse tree produced by trabParser#WhileCond.
    def exitWhileCond(self, ctx:trabParser.WhileCondContext):
        pass


    # Enter a parse tree produced by trabParser#printExpr.
    def enterPrintExpr(self, ctx:trabParser.PrintExprContext):
        pass

    # Exit a parse tree produced by trabParser#printExpr.
    def exitPrintExpr(self, ctx:trabParser.PrintExprContext):
        pass


    # Enter a parse tree produced by trabParser#printSec.
    def enterPrintSec(self, ctx:trabParser.PrintSecContext):
        pass

    # Exit a parse tree produced by trabParser#printSec.
    def exitPrintSec(self, ctx:trabParser.PrintSecContext):
        pass


    # Enter a parse tree produced by trabParser#printFunc.
    def enterPrintFunc(self, ctx:trabParser.PrintFuncContext):
        pass

    # Exit a parse tree produced by trabParser#printFunc.
    def exitPrintFunc(self, ctx:trabParser.PrintFuncContext):
        pass


    # Enter a parse tree produced by trabParser#inputFunc.
    def enterInputFunc(self, ctx:trabParser.InputFuncContext):
        pass

    # Exit a parse tree produced by trabParser#inputFunc.
    def exitInputFunc(self, ctx:trabParser.InputFuncContext):
        pass


    # Enter a parse tree produced by trabParser#BoolTFExpr.
    def enterBoolTFExpr(self, ctx:trabParser.BoolTFExprContext):
        pass

    # Exit a parse tree produced by trabParser#BoolTFExpr.
    def exitBoolTFExpr(self, ctx:trabParser.BoolTFExprContext):
        pass


    # Enter a parse tree produced by trabParser#StringExpr.
    def enterStringExpr(self, ctx:trabParser.StringExprContext):
        pass

    # Exit a parse tree produced by trabParser#StringExpr.
    def exitStringExpr(self, ctx:trabParser.StringExprContext):
        pass


    # Enter a parse tree produced by trabParser#BoolExpr.
    def enterBoolExpr(self, ctx:trabParser.BoolExprContext):
        pass

    # Exit a parse tree produced by trabParser#BoolExpr.
    def exitBoolExpr(self, ctx:trabParser.BoolExprContext):
        pass


    # Enter a parse tree produced by trabParser#FloatExpr.
    def enterFloatExpr(self, ctx:trabParser.FloatExprContext):
        pass

    # Exit a parse tree produced by trabParser#FloatExpr.
    def exitFloatExpr(self, ctx:trabParser.FloatExprContext):
        pass


    # Enter a parse tree produced by trabParser#IdExpr.
    def enterIdExpr(self, ctx:trabParser.IdExprContext):
        pass

    # Exit a parse tree produced by trabParser#IdExpr.
    def exitIdExpr(self, ctx:trabParser.IdExprContext):
        pass


    # Enter a parse tree produced by trabParser#CompExpr.
    def enterCompExpr(self, ctx:trabParser.CompExprContext):
        pass

    # Exit a parse tree produced by trabParser#CompExpr.
    def exitCompExpr(self, ctx:trabParser.CompExprContext):
        pass


    # Enter a parse tree produced by trabParser#CompAllExpr.
    def enterCompAllExpr(self, ctx:trabParser.CompAllExprContext):
        pass

    # Exit a parse tree produced by trabParser#CompAllExpr.
    def exitCompAllExpr(self, ctx:trabParser.CompAllExprContext):
        pass


    # Enter a parse tree produced by trabParser#NegateExpr.
    def enterNegateExpr(self, ctx:trabParser.NegateExprContext):
        pass

    # Exit a parse tree produced by trabParser#NegateExpr.
    def exitNegateExpr(self, ctx:trabParser.NegateExprContext):
        pass


    # Enter a parse tree produced by trabParser#AssignExpr.
    def enterAssignExpr(self, ctx:trabParser.AssignExprContext):
        pass

    # Exit a parse tree produced by trabParser#AssignExpr.
    def exitAssignExpr(self, ctx:trabParser.AssignExprContext):
        pass


    # Enter a parse tree produced by trabParser#IntegerExpr.
    def enterIntegerExpr(self, ctx:trabParser.IntegerExprContext):
        pass

    # Exit a parse tree produced by trabParser#IntegerExpr.
    def exitIntegerExpr(self, ctx:trabParser.IntegerExprContext):
        pass


    # Enter a parse tree produced by trabParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:trabParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by trabParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:trabParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by trabParser#PlusExpr.
    def enterPlusExpr(self, ctx:trabParser.PlusExprContext):
        pass

    # Exit a parse tree produced by trabParser#PlusExpr.
    def exitPlusExpr(self, ctx:trabParser.PlusExprContext):
        pass


    # Enter a parse tree produced by trabParser#ParensExpr.
    def enterParensExpr(self, ctx:trabParser.ParensExprContext):
        pass

    # Exit a parse tree produced by trabParser#ParensExpr.
    def exitParensExpr(self, ctx:trabParser.ParensExprContext):
        pass


    # Enter a parse tree produced by trabParser#CallExpr.
    def enterCallExpr(self, ctx:trabParser.CallExprContext):
        pass

    # Exit a parse tree produced by trabParser#CallExpr.
    def exitCallExpr(self, ctx:trabParser.CallExprContext):
        pass


    # Enter a parse tree produced by trabParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:trabParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by trabParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:trabParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by trabParser#MinusExpr.
    def enterMinusExpr(self, ctx:trabParser.MinusExprContext):
        pass

    # Exit a parse tree produced by trabParser#MinusExpr.
    def exitMinusExpr(self, ctx:trabParser.MinusExprContext):
        pass



del trabParser