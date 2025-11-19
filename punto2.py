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
            raise ValueError(
                f"No se pueden multiplicar: dimensiones {self.filas}x{self.cols} "
                f"y {otra.filas}x{otra.cols} incompatibles"
            )
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
    
    def __repr__(self):
        return f"Matriz({self.datos})"


if __name__ == "__main__":

    A = Matriz([
        [1, 2, 3],
        [4, 5, 6]
    ])
    
    B = Matriz([
        [1, 0],
        [0, 1],
        [1, 1]
    ])
    
    print("Matriz A:")
    print(A)
    print(f"Dimensiones: {A.filas}x{A.cols}\n")
    
    print("Matriz B:")
    print(B)
    print(f"Dimensiones: {B.filas}x{B.cols}\n")
    
    C = A * B
    print("Resultado A * B:")
    print(C)
    print(f"Dimensiones: {C.filas}x{C.cols}\n")
    
    I = Matriz([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    
    D = Matriz([
        [2, 3, 4],
        [5, 6, 7],
        [8, 9, 10]
    ])
    
    print("Matriz D * Identidad:")
    resultado = D * I
    print(resultado)
    
    print("\nProbando dimensiones incompatibles:")
    try:
        E = Matriz([[1, 2]])
        F = Matriz([[1], [2], [3]])
        G = E * F  # Esto debe fallar
    except ValueError as e:
        print(f"Error capturado: {e}")