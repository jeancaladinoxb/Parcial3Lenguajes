# Generated from punto3.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .punto3Parser import punto3Parser
else:
    from punto3Parser import punto3Parser

# This class defines a complete generic visitor for a parse tree produced by punto3Parser.

class punto3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by punto3Parser#programa.
    def visitPrograma(self, ctx:punto3Parser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto3Parser#parentesis.
    def visitParentesis(self, ctx:punto3Parser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto3Parser#multiplicacion.
    def visitMultiplicacion(self, ctx:punto3Parser.MultiplicacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto3Parser#matrizSola.
    def visitMatrizSola(self, ctx:punto3Parser.MatrizSolaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto3Parser#matriz.
    def visitMatriz(self, ctx:punto3Parser.MatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto3Parser#filas.
    def visitFilas(self, ctx:punto3Parser.FilasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto3Parser#fila.
    def visitFila(self, ctx:punto3Parser.FilaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto3Parser#elementos.
    def visitElementos(self, ctx:punto3Parser.ElementosContext):
        return self.visitChildren(ctx)



del punto3Parser