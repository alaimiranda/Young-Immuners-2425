# **Tema 4. Randomización y listas**
1. Módulo random.
2. Listas.
3. Tamaño de una lista.
4. Elementos de una lista.
5. Proyecto: Selector de nombres aleatorios.

## **1. Módulo random**

El módulo **random** implementa una serie de funciones que nos permiten generar números aleatorios.

Los números aleatorios se utilizan en campos como:

*   Ciberseguridad
*   Videojuegos (Tetris)
*   Juegos de Azar
*   Arte


Para utilizar sus funciones tan solo debemos importar este módulo de la siguiente forma:

```
import random
```

Documentación oficial para consultas: [random](https://docs.python.org/es/3/library/random.html)

### `random.randint(a, b)`

Esta función retorna un número entero aleatorio N tal que a $\le$ N $\le$ b. Es decir, el número aleatorio generado va a estar entre a y b incluidos los dos.

### **Programa 1:**

Modifica el siguiente programa para que se imprima un número aleatorio entre 0 y 150.

```
#Programa1.py

import random

numero_aleatorio = random.randint (1, 10)

print(f"El numero aleatorio es: {numero_aleatorio}")
```

### **Programa 2:**

Escribe un programa que simulará aleatoriamente el lanzamiento de una moneda.
*   El programa generará un número entero aleatorio entre el 0 y el 1.
    *   Si el número aleatorio es 0 imprimirá cara.
    *   Si el número aleatorio es 1 imprimirá cruz.

**Ejemplos de ejecución:**

    El numero aleatorio es: 0.
    En la moneda ha salido cara.
---
    El numero aleatorio es: 1.
    En la moneda ha salido cruz.


## **2. Listas**

La primera estructura de datos que veremos son las **listas**. Éstas son un conjunto de elementos ordenados separados por comas y escritos entre corchetes, `[]`.

Las listas son:
- hetereogéneas: los elementos pueden ser de distinto tipo en una misma lista
- mutables: los elementos pueden ser modificados

**Ejemplo de lista:**

```
lista = ["Alba", 12, 1.65, True]
print(f"Mi lista es: {lista} y su tipo es: {type(lista)}")
```

## **3. Tamaño de una lista**

Para saber la longitud o el tamaño de una lista, podemos hacer uso de la función `len()`

```
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
longitud = len(l)
print(f"Longitud: {longitud}")
```

## **4. Elementos de una lista**

Cada elemento en la lista tiene su propio índice.

```
alumnos = ["Maria", "Juan", "Claudia", "Jorge", "Alejandro"]
```

A `María` le corresponde el índice 0; a `Juan`, el 1; a `Claudia` el 2; a `Jorge`, el 3; y a `Alejandro`, el 4.

Dada una lista, podemos acceder a sus elementos utilizando la sintaxis `[]`.

```
print(f"Hoy ha venido a clase: {alumnos[0]}, {alumnos[2]} y {alumnos[4]}")
```

**¡Cuidado!** En `Python`, los índices siempre empiezan en 0. De este modo, al primer elemento le corresponde el índice 0; al segundo, el índice 1; y al $n$-ésimo, le corresponde el índice $n−1$.

## **5. Proyecto: Selector de nombres aleatorios**

En este programa vamos a hacer un selector de nombres aleatorios. Los usos que les puedes dar a este programa son diversos:

* Seleccionar un nombre para un bebé.
* Seleccionar a una persona para pagar la cuenta.
* Seleccionar a un ganador para un concurso.

Para ello:
1.   Crea una lista con los nombres entre los que seleccionar.
2.   Obtén la longitud de la lista.
3.   Genera un número entero aleatorio entre 0 y el máximo índice posible de la lista.
4.   Muestra por pantalla el nombre seleccionado.

**Avanzado:** Pide la lista de nombres al usuario con la función `input()`. Para ello busca información en Google sobre la función `split()`



### Ejemplo de matriz

```
claseA = ["Alai", "Paula", "Opi"]
claseB = ["Lolo", "Starks", "Nopi"]
claseC = ["Tati", "Lonlo","Tutifruti"]

clases1 = [claseA, claseB, claseC]

for clase in range(3):
  print(f"En la clase {clase + 1}:")
  for alumno in range(3):
    print(clases1[clase][alumno])
```