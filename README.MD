## Punto 1 

Para el punto uno se desarrolló una función que genera una gramática de atributos para un Lenguaje de programación que realice consultas de tipo SQL, este punto fue desarrollado en Python con funciones de sql básicas como select, insert, update, delete en una base de datos donde se hace uso de claves como where, set, from. Etc...
Se consideró una gramática de atributos que se presenta en el siguiente árbol

![Árbol](Imagenes/02.png)

![Ejecución Punto 1](Imagenes/01.png)

## Punto 2

Este proyecto implementa un sistema de multiplicación de matrices utilizando el concepto de gramática de atributos. Se desarrollaron dos versiones: la primera sigue estrictamente el patrón de traducción dirigida por sintaxis. El código incluye validación de dimensiones, manejo de errores y ejemplos prácticos de uso, demostrando tanto los fundamentos teóricos de las gramáticas de atributos como su aplicación práctica en el procesamiento de estructuras de datos matriciales

![Ejecución Punto 2](Imagenes/03.png)

## Punto 3

En este ejercicio se diseñó una gramática capaz de representar matrices y operaciones de multiplicación entre ellas, y luego se implementó un Visitor en Python para evaluar dichas expresiones. La gramática permite describir matrices con filas y columnas, así como expresiones anidadas y multiplicaciones. Con el Visitor se recorren los nodos del árbol generado por ANTLR, construyendo objetos de matriz y aplicando la regla del producto punto cuando se encuentran operaciones. Finalmente, se ejecutaron varios ejemplos para validar que la multiplicación funciona correctamente y que se detectan errores de dimensiones incompatibles.

![Ejecución Punto 3](Imagenes/04.png)


