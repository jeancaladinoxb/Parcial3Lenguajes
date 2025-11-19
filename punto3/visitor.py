from antlr4 import *
from punto3Lexer import punto3Lexer
from punto3Parser import punto3Parser
from punto3Visitor import punto3Visitor


class Matriz:
    def __init__(self, datos):
        if not datos or not datos[0]:
            raise ValueError("La matriz no puede estar vacía")
        self.datos = datos
        self.filas = len(datos)
        self.cols = len(datos[0])
        for fila in datos:
            if len(fila) != self.cols:
                raise ValueError("Todas las filas deben tener la misma longitud")
    
    def __mul__(self, otra):
        if self.cols != otra.filas:
            raise ValueError(f"Dimensiones incompatibles: {self.filas}x{self.cols} y {otra.filas}x{otra.cols}")
        
        resultado = [[0] * otra.cols for _ in range(self.filas)]
        for i in range(self.filas):
            for j in range(otra.cols):
                for k in range(self.cols):
                    resultado[i][j] += self.datos[i][k] * otra.datos[k][j]
        return Matriz(resultado)
    
    def __str__(self):
        lineas = []
        for fila in self.datos:
            lineas.append("  " + str(fila))
        return "[\n" + ",\n".join(lineas) + "\n]"


class MatrizEvalVisitor(punto3Visitor):
    
    def visitPrograma(self, ctx):
        return self.visit(ctx.expresion())
    
    def visitMatrizSola(self, ctx):
        return self.visit(ctx.matriz())
    
    def visitMultiplicacion(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        return izq * der
    
    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion())
    
    def visitMatriz(self, ctx):
        filas_datos = self.visit(ctx.filas())
        return Matriz(filas_datos)
    
    def visitFilas(self, ctx):
        filas = []
        for fila_ctx in ctx.fila():
            filas.append(self.visit(fila_ctx))
        return filas
    
    def visitFila(self, ctx):
        return self.visit(ctx.elementos())
    
    def visitElementos(self, ctx):
        elementos = []
        for numero in ctx.NUMERO():
            v = float(numero.getText())
            if v.is_integer():
                v = int(v)
            elementos.append(v)
        return elementos


def evaluar_expresion(texto):
    input_stream = InputStream(texto)
    lexer = punto3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = punto3Parser(token_stream)
    tree = parser.programa()
    visitor = MatrizEvalVisitor()
    return visitor.visit(tree)


if __name__ == "__main__":
    
    print("Ejemplo 1: Matriz simple")
    expr1 = "[[1, 2, 3], [4, 5, 6]]"
    print(f"Expresión: {expr1}")
    try:
        resultado1 = evaluar_expresion(expr1)
        print(f"Resultado:\n{resultado1}\n")
    except Exception as e:
        print(f"Error: {e}\n")
    

    print("Ejemplo 2: Multiplicación de matrices")
    expr2 = "[[1, 2], [3, 4]] * [[2, 0], [1, 2]]"
    print(f"Expresión: {expr2}")
    try:
        resultado2 = evaluar_expresion(expr2)
        print(f"Resultado:\n{resultado2}\n")
    except Exception as e:
        print(f"Error: {e}\n")
    

    print("Ejemplo 3: Multiplicación con paréntesis")
    expr3 = "([[1, 0], [0, 1]] * [[2, 3], [4, 5]]) * [[1], [1]]"
    print(f"Expresión: {expr3}")
    try:
        resultado3 = evaluar_expresion(expr3)
        print(f"Resultado:\n{resultado3}\n")
    except Exception as e:
        print(f"Error: {e}\n")
    

    print("Ejemplo 4: Error de dimensiones incompatibles")
    expr4 = "[[1, 2, 3]] * [[1, 2], [3, 4]]"
    print(f"Expresión: {expr4}")
    try:
        resultado4 = evaluar_expresion(expr4)
        print(f"Resultado:\n{resultado4}\n")
    except Exception as e:
        print(f"Error: {e}\n")


