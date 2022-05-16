from antlr4 import *
from gen.trabLexer import trabLexer
from trabListener import trabListener
from gen.trabParser import trabParser
import os
import subprocess

file = open("prog.py", "r");
data = InputStream(file.read())
# data = FileStream('prog.txt')
lexer = trabLexer(data)
stream = CommonTokenStream(lexer)

parser = trabParser(stream)
tree = parser.prog()

listener = trabListener()

ParseTreeWalker().walk(listener, tree)
os.system('"java -jar .\jasmin.jar trab.j"')
print("Compilado com sucesso")


#print(data)

