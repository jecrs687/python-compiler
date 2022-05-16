# Generated from C:/Users/Gabriel Soares/PycharmProjects/ANTLR CSV to JSON\trab.g4 by ANTLR 4.9.2
import random

from antlr4 import *

if __name__ is not None and "." in __name__:
    from gen.trabParser import trabParser
else:
    from gen.trabParser import trabParser


# This class defines a complete listener for a parse tree produced by trabParser.
class trabListener(ParseTreeListener):
    ids = [[]]
    input = False
    valueIf = 0
    ifs = [[]]
    condsLabels = [[]]
    funcsName = [[]]
    func = 0
    labels = """"
    """
    prog = [[]]

    def tipo(self, value):
        if value == 0:
            return "int"
        if value == 1:
            return "float"
        if value == 2:
            return "boolean"
        if value == 3:
            return "string"
        return "void"

    def tipoToNumber(self, value):
        if value == "int":
            return 0
        if value == "float":
            return 1
        if value == "boolean":
            return 2
        if value == "string":
            return 3
        return 4

    # Enter a parse tree produced by trabParser#prog.
    def enterProg(self, ctx: trabParser.ProgContext):

        pass

    # Exit a parse tree produced by trabParser#prog.
    def exitProg(self, ctx: trabParser.ProgContext):
        if self.input:
            self.condsLabels.append([])
            self.prog.append([""".method public static read()I
    
               .limit stack 5   ; up to five items can be pushed
               .limit locals 100
    
               ; the input function starts at this point
                ldc 0
                istore 50     ; storage for a dummy integer for reading it by input()
                ldc 0
                istore 49     ; preparacao para negativo
             Label1:
                getstatic java/lang/System/in Ljava/io/InputStream;
                invokevirtual java/io/InputStream/read()I
                istore 51
                iload 51
              ;  ldc 10 ; uso no mac (valor ASCII da tecla ENTER)
                ldc 13 ; uso no windows (valor ASCII da tecla ENTER)
                isub
                ifeq Label2
                iload 51
                ldc 32 ; space 
                isub
                ifeq Label2
                iload 51
                ldc 43 ; plus sign
                isub
                ifeq Label1
                iload 51
                ldc 45 ; minus sign
                isub
                ifeq Label3
                iload 51
                ldc 48
                isub
                ldc 10
                iload 50
                imul
                iadd
                istore 50
                goto Label1
    
              Label3:
                ldc 1
                istore 49
                goto Label1
    
              Label2:     ; now our dummy integer contains the integer read from the keyboard
                ldc 1
                iload 49
                isub
                ifeq Label4
                iload 50       ; input function ends here
                ireturn
              Label4:
                ldc 0
                iload 50
                isub
                ireturn
            .end method"""])

        y = """
        .class public trabCompiladores
        .super java/lang/Object
        """
        self.prog.reverse()
        for x in self.prog:
            for d in x:
                y = y + d
        x = open("trab.j", "w")
        x.write(y)
        pass

    # Enter a parse tree produced by trabParser#listaDecVars.
    def enterListaDecVars(self, ctx: trabParser.ListaDecVarsContext):

        pass

    # Exit a parse tree produced by trabParser#listaDecVars.
    def exitListaDecVars(self, ctx: trabParser.ListaDecVarsContext):
        ctx.value = ctx.children[0].value
        pass

    # Enter a parse tree produced by trabParser#decVars.
    def enterDecVars(self, ctx: trabParser.DecVarsContext):
        pass

    # Exit a parse tree produced by trabParser#decVars.
    def exitDecVars(self, ctx: trabParser.DecVarsContext):
        for i in ctx.listaDecVars().value:
            if not (i[2] == None):
                tipo = ctx.tipo().value
                tipoId = self.tipo(i[2])
                if tipo != tipoId:
                    raise ValueError(f"Erro na declaraçao do tipo {tipo} != {tipoId} na declaração de  {i[0]}")
                    return;
            else:
                tipo = ctx.tipo().value
                tipo = self.tipoToNumber(tipo)
                for x in self.ids[self.func]:
                    if x[0] == i[0]:
                        index = self.ids[self.func].index(i)
                        self.ids[self.func][index] = [i[0], None, tipo]

        pass

    # Enter a parse tree produced by trabParser#decParam.
    def enterDecParam(self, ctx: trabParser.DecParamContext):
        pass

    # Exit a parse tree produced by trabParser#decParam.
    def exitDecParam(self, ctx: trabParser.DecParamContext):
        i = str(ctx.ID())
        for x in self.ids[self.func]:
            if i == x[0]:
                raise ValueError(f"Variável {x[0]} já declarada")
                return
        self.ids[self.func].append([i, None, self.tipoToNumber(ctx.tipo().getText())])
        pass

    # Enter a parse tree produced by trabParser#tipo.
    def enterTipo(self, ctx: trabParser.TipoContext):
        pass

    # Exit a parse tree produced by trabParser#tipo.
    def exitTipo(self, ctx: trabParser.TipoContext):
        ctx.value = ctx.getText()
        pass

    # Enter a parse tree produced by trabParser#listaIds.
    def enterListaIds(self, ctx: trabParser.ListaIdsContext):
        for i in ctx.ID():
            i = str(i)
            for x in self.ids[self.func]:
                if i == x[0]:
                    raise ValueError("Erro: Variaveis já declarada")
                    return
            self.ids[self.func].append([i, None, None])
        pass

    # Exit a parse tree produced by trabParser#listaIds.
    def exitListaIds(self, ctx: trabParser.ListaIdsContext):
        x = []
        for i in ctx.ID():
            i = str(i)
            payload = [i, None, None]
            x.append(payload)
        ctx.value = x

        pass

    # Enter a parse tree produced by trabParser#atrib.
    def enterAtrib(self, ctx: trabParser.AtribContext):
        i = str(ctx.ID())
        for x in self.ids[self.func]:
            if i == x[0]:
                raise ValueError(f"Variável {x[0]} já declarada")
                return
        self.ids[self.func].append([i, None, None])
        pass

    # Exit a parse tree produced by trabParser#atrib.
    def exitAtrib(self, ctx: trabParser.AtribContext):
        x = []
        i = ctx.ID()
        i = str(i)
        payload = [i, None, None]
        x.append(payload)
        self.ids[self.func].remove(payload)
        payload[1] = ctx.expr().value[1]
        payload[2] = ctx.expr().value[2]
        self.ids[self.func].append(payload)
        ctx.value = x
        if (payload[2] == 0):
            self.prog[self.func].append(f"""
        istore {self.ids[self.func].index(payload)}
        """)
        if (payload[2] == 1):
            self.prog[self.func].append(f"""
        fstore {self.ids[self.func].index(payload)}
        """)
        if (payload[2] == 2):
            self.prog[self.func].append(f"""
        astore {self.ids[self.func].index(payload)}
        """)
        if (payload[2] == 3):
            self.prog[self.func].append(f"""
        astore {self.ids[self.func].index(payload)}
            """)

        pass

    # Enter a parse tree produced by trabParser#listaAtribs.
    def enterListaAtribs(self, ctx: trabParser.ListaAtribsContext):

        pass

    # Exit a parse tree produced by trabParser#listaAtribs.
    def exitListaAtribs(self, ctx: trabParser.ListaAtribsContext):
        x = []
        for i in ctx.atrib():
            for y in i.value:
                x.append(y)
        ctx.value = x
        pass

    # Enter a parse tree produced by trabParser#tipoFunc.
    def enterTipoFunc(self, ctx: trabParser.TipoFuncContext):
        pass

    # Exit a parse tree produced by trabParser#tipoFunc.
    def exitTipoFunc(self, ctx: trabParser.TipoFuncContext):
        pass

    # Enter a parse tree produced by trabParser#DecFunc.
    def enterDecFunc(self, ctx: trabParser.DecFuncContext):
        self.prog.append([])
        self.func = self.func + 1;
        self.ids.append([])
        self.condsLabels.append([])
        self.ifs.append([])
        dic={
            "int":"I",
            "float":"F",
        }
        y = ""

        tipo = dic[ctx.tipoFunc().getText()]
        self.funcsName.append([ctx.ID(),tipo])

        for x in ctx.decParam():
            y = y+ dic[x.tipo().getText()]
        self.prog[self.func].append(f"""
.method public static {ctx.ID()}({y}){tipo}
.limit stack 50
.limit locals 50""")
        pass

    # Exit a parse tree produced by trabParser#DecFunc.
    def exitDecFunc(self, ctx: trabParser.DecFuncContext):
        dic={
            "int":"ireturn",
            "float":"freturn",
            "void":"",
            "string":"areturn"
        }
        tipo = dic[str(ctx.tipoFunc().getText())]
        self.prog[self.func].append(f"""
        {tipo}""")
        for x in self.condsLabels[self.func]:
            for t in x:
                self.prog[self.func].append(t)

        self.prog[self.func].append("""
        .end method""")

        pass

    # Enter a parse tree produced by trabParser#returnFunc.
    def enterReturnFunc(self, ctx: trabParser.ReturnFuncContext):
        pass

    # Exit a parse tree produced by trabParser#returnFunc.
    def exitReturnFunc(self, ctx: trabParser.ReturnFuncContext):
        self.prog[self.func].append("""
        ireturn
               """)
        pass

    # Enter a parse tree produced by trabParser#blocoMain.
    def enterBlocoMain(self, ctx: trabParser.BlocoMainContext):
        self.prog.append([])
        self.func = 0
        self.condsLabels.append([])
        self.ifs.append([])
        self.prog[self.func] = ["""
.method public static main([Ljava/lang/String;)V
.limit stack 50
.limit locals 50"""] + self.prog[self.func]
        pass

    # Exit a parse tree produced by trabParser#blocoMain.
    def exitBlocoMain(self, ctx: trabParser.BlocoMainContext):
        self.prog[self.func].append("""
    return""")
        for x in self.condsLabels[self.func]:
            for t in x:
                self.prog[self.func].append(t)

        self.prog[self.func].append("""
    .end method""")

        pass

    # Enter a parse tree produced by trabParser#stmts.
    def enterStmts(self, ctx: trabParser.StmtsContext):
        pass

    # Exit a parse tree produced by trabParser#stmts.
    def exitStmts(self, ctx: trabParser.StmtsContext):
        pass

    # Enter a parse tree produced by trabParser#stmts_break.
    def enterStmts_break(self, ctx: trabParser.Stmts_breakContext):
        pass

    # Exit a parse tree produced by trabParser#stmts_break.
    def exitStmts_break(self, ctx: trabParser.Stmts_breakContext):
        pass

    # Enter a parse tree produced by trabParser#callFunction.
    def enterCallFunction(self, ctx: trabParser.CallFunctionContext):

        pass

    # Exit a parse tree produced by trabParser#callFunction.
    def exitCallFunction(self, ctx: trabParser.CallFunctionContext):
        y = ""
        for x in ctx.expr():
            y="I"+y
        self.prog[self.func].append(f"""
        invokestatic trabCompiladores.{ctx.ID()}({y})I
        """
        )
        pass

    # Enter a parse tree produced by trabParser#cmdAtrib.
    def enterCmdAtrib(self, ctx: trabParser.CmdAtribContext):
        pass

    # Exit a parse tree produced by trabParser#cmdAtrib.
    def exitCmdAtrib(self, ctx: trabParser.CmdAtribContext):
        x = str(ctx.ID())
        y = ctx.expr().value
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]
        existe = False
        for i in self.ids[self.func]:
            if (i[0] == x):
                existe=True
                if y in vars:
                    if i[2] != y[0]:
                        raise ValueError(f"Tipo de {i[0]} ({self.tipo(i[2])}) incompatível com {self.tipo(y[0])}")
                else:
                    if i[2] != y[2]:
                        raise ValueError(f"Tipo de {i[0]} ({self.tipo(i[2])}) incompatível com {self.tipo(y[2])}")
                if i[2] == 0:
                    self.prog[self.func].append(f"""
        istore {self.ids[self.func].index(i)}
""")
                if i[2] == 1:
                    self.prog[self.func].append(f"""
        fstore {self.ids[self.func].index(i)}
        """)
                if i[2] == 3:
                    self.prog[self.func].append(f"""
        astore {self.ids[self.func].index(i)}
        """)
        if not existe:
            raise ValueError(f"variável {x} não declarada")
        pass

    # Enter a parse tree produced by trabParser#IfCond.
    def enterIfCond(self, ctx: trabParser.IfCondContext):
        pass

    # Exit a parse tree produced by trabParser#IfCond.
    def exitIfCond(self, ctx: trabParser.IfCondContext):
        y  = self.ifs[self.func].pop()

        self.prog[self.func].append(f"""
        Retorno{y[1]}:
            """)
        pass

    # Enter a parse tree produced by trabParser#IfBreakCond.
    def enterIfBreakCond(self, ctx: trabParser.IfBreakCondContext):
        pass

    # Exit a parse tree produced by trabParser#IfBreakCond.
    def exitIfBreakCond(self, ctx: trabParser.IfBreakCondContext):
        y = self.ifs[self.func].pop()
        x = [f"""
        goto Retorno{y[1]}
            """]
        while len(self.prog[self.func]) - y[0] != 0:
            x.append(self.prog[self.func].pop())
        x.append(f"""
    Cond{y[1]}:""")
        x.reverse()
        self.condsLabels[self.func].append(x)
        self.prog[self.func].append(f"""
        Retorno{y[1]}:
                  """)
        pass

    # Enter a parse tree produced by trabParser#ForCond.
    def enterForCond(self, ctx: trabParser.ForCondContext):
        self.valueIf = self.valueIf + 1
        try:
            self.prog[self.func].append(f"""
        ldc {int(ctx.e1.text)}""")
        except:
            for x in self.ids[self.func]:
                if x[0] == ctx.e1.text:
                    self.prog[self.func].append(f"""
        iload {self.ids[self.func].index(x)}""")
        for x in self.ids[self.func]:
            if x[0]==ctx.ID()[0].getText():
                if x[2] !=0:
                    raise ValueError(f"Tipo de {x[0]} incompatível com a operação FOR")
                self.prog[self.func].append(f"""
        istore {self.ids[self.func].index(x)}""")
                self.prog[self.func].append(f"""
        iload {self.ids[self.func].index(x)}""")
        try:
            self.prog[self.func].append(f"""
        ldc {int(ctx.e2.text)}""")
        except:
            for x in self.ids[self.func]:
                if x[0] == ctx.e2.text:
                    self.prog[self.func].append(f"""
        iload {self.ids[self.func].index(x)}""")
        self.prog[self.func].append(f"""
        if_icmplt For{ self.valueIf}
        Retorno{ self.valueIf}:
        """)
        self.ifs[self.func].append([len(self.prog[self.func]), self.valueIf])
        pass

    # Exit a parse tree produced by trabParser#ForCond.
    def exitForCond(self, ctx: trabParser.ForCondContext):
        y = self.ifs[self.func][len(self.ifs[self.func]) - 1]
        x =[]
        while len(self.prog[self.func]) - y[0] != 0:
            x.append(self.prog[self.func].pop())
        x.append(f"""
        For{y[1]}: 
                """)
        x.reverse()
        x.append(f"""
        {self.prog[self.func][len(self.prog[self.func])-3]}
        ldc 1
        iadd
        {self.prog[self.func][len(self.prog[self.func])-4]}
        {self.prog[self.func][len(self.prog[self.func])-3]}
        {self.prog[self.func][len(self.prog[self.func])-2]}
        if_icmplt For{y[1]}
        goto Retorno{y[1]}
                """)
        self.condsLabels[self.func].append(x)
        pass


    # Enter a parse tree produced by trabParser#WhileCond.
    def enterWhileCond(self, ctx: trabParser.WhileCondContext):
        pass

    # Exit a parse tree produced by trabParser#WhileCond.
    def exitWhileCond(self, ctx: trabParser.WhileCondContext):
        y = self.ifs[self.func].pop()
        x = [f"""{self.prog[self.func][y[0] - 3]}{self.prog[self.func][y[0] - 2]}{self.prog[self.func][y[0] - 1]}
        goto Retorno{y[1]}"""]
        while len(self.prog[self.func]) - y[0] != 0:
            x.append(self.prog[self.func].pop())
        x.append(f"""
    Cond{y[1]}:""")
        x.reverse()
        self.condsLabels[self.func].append(x)
        self.prog[self.func].append(f"""
        Retorno{y[1]}:
                  """)
        pass

    # Enter a parse tree produced by trabParser#printFunc.
    def enterPrintFunc(self, ctx: trabParser.PrintFuncContext):

        pass

    # Exit a parse tree produced by trabParser#printFunc.
    def exitPrintFunc(self, ctx: trabParser.PrintFuncContext):


        pass

    # Enter a parse tree produced by trabParser#inputFunc.
    def enterInputFunc(self, ctx: trabParser.InputFuncContext):
        self.input = True

        pass

    # Exit a parse tree produced by trabParser#inputFunc.
    def exitInputFunc(self, ctx: trabParser.InputFuncContext):
        x = str(ctx.ID());
        existe = False
        for i in self.ids[self.func]:
            if i[0] == x:
                existe = True
                self.prog[self.func].append(f"""
        invokestatic trabCompiladores.read()I
        istore {self.ids[self.func].index(i)}
                """)
                ctx.value = i
        if not existe:
            raise ValueError(f"Variável {x} não declarada")
        pass


    # Enter a parse tree produced by trabParser#BoolTFExpr.
    def enterBoolTFExpr(self, ctx: trabParser.BoolTFExprContext):
        pass

    # Exit a parse tree produced by trabParser#BoolTFExpr.
    def exitBoolTFExpr(self, ctx: trabParser.BoolTFExprContext):
        x = str(ctx.BOOL())
        ctx.value = [None, bool(x), 2]
        pass

    # Enter a parse tree produced by trabParser#StringExpr.
    def enterStringExpr(self, ctx: trabParser.StringExprContext):
        pass

    # Exit a parse tree produced by trabParser#StringExpr.
    def exitStringExpr(self, ctx: trabParser.StringExprContext):
        x = str(ctx.STRING())
        self.prog[self.func].append(f"""
        ldc {x}""")
        ctx.value = [None, x, 3]
        pass

    # Enter a parse tree produced by trabParser#BoolExpr.
    def enterBoolExpr(self, ctx: trabParser.BoolExprContext):
        pass

    # Exit a parse tree produced by trabParser#BoolExpr.
    def exitBoolExpr(self, ctx: trabParser.BoolExprContext):
        pass

    # Enter a parse tree produced by trabParser#FloatExpr.
    def enterFloatExpr(self, ctx: trabParser.FloatExprContext):
        pass

    # Exit a parse tree produced by trabParser#FloatExpr.
    def exitFloatExpr(self, ctx: trabParser.FloatExprContext):
        x = float(str(ctx.FLOAT()))
        self.prog[self.func].append(f"""
        ldc {x}""")
        ctx.value = [None, x, 1]
        pass

    # Enter a parse tree produced by trabParser#IdExpr.
    def enterIdExpr(self, ctx: trabParser.IdExprContext):
        pass

    # Exit a parse tree produced by trabParser#IdExpr.
    def exitIdExpr(self, ctx: trabParser.IdExprContext):
        x = str(ctx.ID())
        for i in self.ids[self.func]:
            if (x == i[0]):
                ctx.value = i
                if i[2] == 0:
                    self.prog[self.func].append(f"""
        iload {self.ids[self.func].index(i)}""")
                if i[2] == 1:
                    self.prog[self.func].append(f"""
        fload {self.ids[self.func].index(i)} """)
                if i[2] == 2:
                    self.prog[self.func].append(f"""
        aload {self.ids[self.func].index(i)}""")
                if i[2] == 3:
                    self.prog[self.func].append(f"""
        aload {self.ids[self.func].index(i)}""")

        pass

    # Enter a parse tree produced by trabParser#CompExpr.
    def enterCompExpr(self, ctx: trabParser.CompExprContext):
        pass

    # Exit a parse tree produced by trabParser#CompExpr.
    def exitCompExpr(self, ctx: trabParser.CompExprContext):
        e2 = ctx.e2.value
        e1 = ctx.e1.value
        x = ctx.op.text
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]
        indexE1 = 2
        indexE2 = 2
        if e1 in vars:
            indexE1 = 0
            ctx.value = e1
        if e2 in vars:
            indexE2 = 0
            ctx.value = e2
        if not (e1 in vars) and not (e2 in vars):
            ctx.value = [e1[2], self.tipo(e1[2])]
        if e1[indexE1] != e2[indexE2]:
            raise ValueError(
                f"Variável {e1[0] or e1[1]} e {e2[0] or e2[1]} com tipos incompatíveis para operação {ctx.op.text} ")
            return
        if e1[indexE1] in [1, 2, 3]:
            raise ValueError(f"tipo {self.tipo(e1[indexE1])} incompatível com operação {ctx.op.text}")
            return
        self.valueIf = self.valueIf + 1
        self.ifs[self.func].append([len(self.prog[self.func])+1, self.valueIf])
        if x == ">":
            self.prog[self.func].append(f"""
        if_icmpgt Cond{self.ifs[self.func][len(self.ifs[self.func]) - 1][1]}
            """)
        if x == "<":
            self.prog[self.func].append(f"""
        if_icmplt Cond{self.ifs[self.func][len(self.ifs[self.func]) - 1][1]}       
            """)
        if x == ">=":
            self.prog[self.func].append(f"""
        if_icmpge Cond{self.ifs[self.func][len(self.ifs[self.func]) - 1][1]}   
            """)
        if x == "<=":
            self.prog[self.func].append(f"""
        if_icmple Cond{self.ifs[self.func][len(self.ifs[self.func]) - 1][1]}     
            """)
        pass

    # Enter a parse tree produced by trabParser#CompAllExpr.
    def enterCompAllExpr(self, ctx: trabParser.CompAllExprContext):
        pass

    # Exit a parse tree produced by trabParser#CompAllExpr.
    def exitCompAllExpr(self, ctx: trabParser.CompAllExprContext):
        e2 = ctx.e2.value
        e1 = ctx.e1.value
        x = ctx.op.text
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]
        indexE1 = 2
        indexE2 = 2
        if e1 in vars:
            indexE1 = 0
            ctx.value = e1
        if e2 in vars:
            indexE2 = 0
            ctx.value = e2
        if not (e1 in vars) and not (e2 in vars):
            ctx.value = [e1[2], self.tipo(e1[2])]
        if e1[indexE1] != e2[indexE2]:
            raise ValueError(
                f"Variável {e1[0] or e1[1]} e {e2[0] or e2[1]} com tipos incompatíveis para operação {ctx.op.text} ")
            return
        if e1[indexE1] in [1, 2, 3]:
            raise ValueError(f"tipo {self.tipo(e1[indexE1])} incompatível com operação {ctx.op.text}")
            return
        self.valueIf = self.valueIf + 1
        self.ifs[self.func].append([len(self.prog[self.func]) + 2, self.valueIf])
        if x == "==":
            self.prog[self.func].append(f"""
              if_icmpeq Cond{self.ifs[self.func][len(self.ifs[self.func]) - 1][1]}
                  """)
        if x == "!=":
            self.prog[self.func].append(f"""
              if_icmpne Cond{self.ifs[self.func][len(self.ifs[self.func]) - 1][1]}       
                  """)
        pass

    # Enter a parse tree produced by trabParser#NegateExpr.
    def enterNegateExpr(self, ctx: trabParser.NegateExprContext):
        pass

    # Exit a parse tree produced by trabParser#NegateExpr.
    def exitNegateExpr(self, ctx: trabParser.NegateExprContext):
        pass

    # Enter a parse tree produced by trabParser#AssignExpr.
    def enterAssignExpr(self, ctx: trabParser.AssignExprContext):
        pass

    # Exit a parse tree produced by trabParser#AssignExpr.
    def exitAssignExpr(self, ctx: trabParser.AssignExprContext):
        pass

    # Enter a parse tree produced by trabParser#IntegerExpr.
    def enterIntegerExpr(self, ctx: trabParser.IntegerExprContext):
        pass

    # Exit a parse tree produced by trabParser#IntegerExpr.
    def exitIntegerExpr(self, ctx: trabParser.IntegerExprContext):
        x = int(str(ctx.INT()))
        self.prog[self.func].append(f"""
        ldc {x}""")
        ctx.value = [None, x, 0]
        pass

    # Enter a parse tree produced by trabParser#MulDivExpr.
    def enterMulDivExpr(self, ctx: trabParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by trabParser#MulDivExpr.
    def exitMulDivExpr(self, ctx: trabParser.MulDivExprContext):
        e2 = ctx.e2.value
        e1 = ctx.e1.value
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]
        indexE1 = 2
        indexE2 = 2
        if e1 in vars:
            indexE1 = 0
            ctx.value = e1
        if e2 in vars:
            indexE2 = 0
            ctx.value = e2
        if not (e1 in vars) and not (e2 in vars):
            ctx.value = [e1[2], self.tipo(e1[2])]
        if e1[indexE1] != e2[indexE2]:
            raise ValueError(
                f"Variável {e1[0] or e1[1]} e {e2[0] or e2[1]} com tipos incompatíveis para operação {ctx.op.text} ")
            return
        if e1[indexE1] in [2, 3]:
            raise ValueError(f"tipo {self.tipo(e1[indexE1])} incompátivel com operação {ctx.op.text}")
            return

        if ctx.op.text == "*":
            if (e1[indexE1] == 0 or e2[indexE2] == 0):
                self.prog[self.func].append(f"""
        imul""")
            if (e1[indexE1] == 1 or e2[indexE2] == 1):
                self.prog[self.func].append(f"""
        fmul""")
        else:
            if (e1[indexE1] == 0 or e2[indexE2] == 0):
                self.prog[self.func].append(f"""
        idiv""")
            if (e1[indexE1] == 1 or e2[indexE2] == 1):
                self.prog[self.func].append(f"""
        fdiv""")
        pass

    # Enter a parse tree produced by trabParser#PlusExpr.
    def enterPlusExpr(self, ctx: trabParser.PlusExprContext):
        pass

    # Exit a parse tree produced by trabParser#PlusExpr.
    def exitPlusExpr(self, ctx: trabParser.PlusExprContext):
        pass

    # Enter a parse tree produced by trabParser#ParensExpr.
    def enterParensExpr(self, ctx: trabParser.ParensExprContext):
        pass

    # Exit a parse tree produced by trabParser#ParensExpr.
    def exitParensExpr(self, ctx: trabParser.ParensExprContext):
        e1 = ctx.expr().value
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]
        if e1 in vars:
            ctx.value = e1
        if not (e1 in vars) :
            ctx.value = [e1[2], self.tipo(e1[2])]
        pass

    # Enter a parse tree produced by trabParser#CallExpr.
    def enterCallExpr(self, ctx: trabParser.CallExprContext):
        pass

    # Exit a parse tree produced by trabParser#CallExpr.
    def exitCallExpr(self, ctx: trabParser.CallExprContext):
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]
        ctx.value=vars[0]
        pass

    # Enter a parse tree produced by trabParser#AddSubExpr.
    def enterAddSubExpr(self, ctx: trabParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by trabParser#AddSubExpr.
    def exitAddSubExpr(self, ctx: trabParser.AddSubExprContext):
        e2 = ctx.e2.value
        e1 = ctx.e1.value
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]
        indexE1 = 2
        indexE2 = 2
        if e1 in vars:
            indexE1 = 0
            ctx.value = e1
        if e2 in vars:
            indexE2 = 0
            ctx.value = e2
        if not (e1 in vars) and not (e2 in vars):
            ctx.value = [e1[2], self.tipo(e1[2])]
        if e1[indexE1] != e2[indexE2]:
            raise ValueError(
                f"Variável {e1[0] or e1[1]} e {e2[0] or e2[1]} com tipos incompatíveis para operação {ctx.op.text} ")
            return
        if e1[indexE1] in [2, 3]:
            raise ValueError(f"tipo {self.tipo(e1[indexE1])} incompátivel com operação {ctx.op.text}")
            return

        if ctx.op.text == "+":
            if (e1[indexE1] == 0 or e2[indexE2] == 0):
                self.prog[self.func].append(f"""
        iadd""")
            if (e1[indexE1] == 1 or e2[indexE2] == 1):
                self.prog[self.func].append(f"""
        fadd""")
        else:
            if (e1[indexE1] == 0 or e2[indexE2] == 0):
                self.prog[self.func].append(f"""
        isub""")
            if (e1[indexE1] == 1 or e2[indexE2] == 1):
                self.prog[self.func].append(f"""
        fsub""")
        pass

    # Enter a parse tree produced by trabParser#MinusExpr.
    def enterMinusExpr(self, ctx: trabParser.MinusExprContext):
        pass

    # Exit a parse tree produced by trabParser#MinusExpr.
    def exitMinusExpr(self, ctx: trabParser.MinusExprContext):
        pass

    # Enter a parse tree produced by trabParser#elseIf.
    def enterElseIf(self, ctx: trabParser.ElseIfContext):
        y = self.ifs[self.func][len(self.ifs[self.func])-1]
        self.prog[self.func].append(f"""
        goto Else{y[1]}
        """)
        self.ifs[self.func][len(self.ifs[self.func])-1][0] = len(self.prog[self.func])
        pass

    # Exit a parse tree produced by trabParser#elseIf.
    def exitElseIf(self, ctx: trabParser.ElseIfContext):
        y = self.ifs[self.func][len(self.ifs[self.func])-1]
        x = [f"""
        goto Retorno{y[1]}
            """]
        while len(self.prog[self.func]) - y[0] != 0:
            x.append(self.prog[self.func].pop())
        x.append(f"""
        Else{y[1]}:""")
        x.reverse()
        self.condsLabels[self.func].append(x)
        pass

    # Enter a parse tree produced by trabParser#normalIf.
    def enterNormalIf(self, ctx: trabParser.NormalIfContext):
        pass

    # Exit a parse tree produced by trabParser#normalIf.
    def exitNormalIf(self, ctx: trabParser.NormalIfContext):
        y = self.ifs[self.func][len(self.ifs[self.func])-1]
        x = [f"""
        goto Retorno{y[1]}
            """]
        while len(self.prog[self.func]) - y[0] != 0:
            x.append(self.prog[self.func].pop())
        x.append(f"""
        Cond{y[1]}:""")
        x.reverse()
        self.condsLabels[self.func].append(x)
        self.prog[self.func].append(f"""
        Retorno{y[1]}:
                  """)
        pass

    # Enter a parse tree produced by trabParser#printSec.
    def enterPrintSec(self, ctx: trabParser.PrintSecContext):
        pass

    # Exit a parse tree produced by trabParser#printSec.
    def exitPrintSec(self, ctx: trabParser.PrintSecContext):
        pass
    # Enter a parse tree produced by trabParser#printSec.
    def enterPrintExpr(self, ctx: trabParser.PrintSecContext):
        self.prog[self.func].append("""
        getstatic java/lang/System/out Ljava/io/PrintStream;""")
        pass

    # Exit a parse tree produced by trabParser#printSec.
    def exitPrintExpr(self, ctx: trabParser.PrintSecContext):
        vars = [[0, "int"], [1, "float"], [2, "boolean"], [3, "string"]]

        x = ctx.expr()
        y = x.value
        index = 2
        if y in vars:
            index = 0
            # raise ValueError("Tipo incompatível com print")
        if y[0] == None or index != 2:
            if y[index] == 0:
                self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(I)V
    """)
            if y[index] == 1:
                self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(F)V
    """)
            if y[index] == 2:
                self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
    """)
            if y[index] == 3:
                self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
    """)
        for d in self.ids[self.func]:
            if (d[0] == y[0]):
                if d[2] == 0:
                    self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(I)V
        """)
                if d[2] == 1:
                    self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(F)V
        """)
                if d[2] == 3:
                    self.prog[self.func].append(f"""
        invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
        """)
        pass


del trabParser