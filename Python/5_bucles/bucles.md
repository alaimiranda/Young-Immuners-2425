# **Tema 5. Bucles**
1. Introducción
2. Bucle for.
3. Bucle while.
4. Proyecto: Generador de contraseñas aleatorias.

## **1. Introducción**

Un **bucle** es una secuencia que repite varias veces un mismo trozo de código, hasta que la condición asignada al bucle deja de cumplirse.

Los bucles son una de las herramientas más importantes en un lenguaje de programación. Éstos nos permiten automatizar tareas repetitivas y escribirlas utilizando muy poquitas líneas de código.

Los bucles que vamos a utilizar en Python son:
*   Bucle `for`
*   Bucle `while`

## **2. Bucle `for`**

La idea del bucle `for` es: para todos los elementos de una secuencia, seguimos realizando las líneas del bucle. Una vez nos quedemos sin elementos, salimos del bucle.

Ejemplos de secuencias iterables:
*   Lista
*   String

Su estructura es la siguiente:
```
for elemento in secuencia:
  instrucción
```

Ejecución:

    instrucción 1
    instrucción 2
    instrucción 3
    ·
    .
    .
    instrucción n


**Observación.** Vuelven a aparecer tanto los dos puntos después de la clave como la indentación previa a las instrucciones que se encuentran dentro del bucle.

Un ejemplo del uso de un bucle `for` es el de recorrer todos los caracteres de un string:

```
cadena = "Me encanta programar"

for i in cadena:
    print(i)
```

Lo que hace el anterior chunk de código es imprimir todos y cada uno de los caracteres, a los que identificamos por `caracter`, que se encuentran en el string `cadena`.

### **Programa 1:**

Dadas las siguientes lista consigue la ejecución deseada utilizando un bucle `for` y la función `print()`.

Ejemplo de ejecución:
    Tarta de manzana.
    Tarta de queso.
    Tarta de zanahoria.
    Tarta de Nutella.
    Tarta de fresa.

```
#Programa1.py
```

### **Programa 2:**

Crea un programa que a partir de una lista de numeros enteros imprima el máximo y el mínimo valor.

La dificultad de este programa es: **Súper chungo**.

Ejemplo de ejecución:
    lista = [33, 27, 99, 22, 45, 54]
    El maximo valor es: 99 y el minimo es: 22

**Nota:** Puedes introducir la lista en el programa o bien pedirle los números al usuario con la función `input()`

```
#Programa2.py
```

### Función `range()`

La función `range()` tiene 3 posibles argumentos en este orden:

 - `start`: Nº comienzo.
 - `stop`: Nº final. **No se incluye**
 - `step`: Paso. Si es negativo cuenta hacia atrás.

Veremos el uso de la función `range()` con un ejemplo en el que imprimiremos los numeros del 0 al 30 contando de 3 en 3:


```
#start: 0
#stop: 31 --> Para que termine en 30.
#step: 3 --> Contando de 3 en 3.
for i in range(0, 31, 3):
  print(i)
```

**Observación.** Cosas a tener en cuenta cuando usamos la función `range()`:

- El elemento indicado en el argumento `stop` nunca se incluye. Si queremos contar hasta 30 hay que poner 31.
- Si no indicamos ningún elemento en el argumento `start`, por defecto éste vale 0.
- El valor por defecto del argumento `step` es 1.

### **Programa 3:**
Codifica un programa que cuente desde el 10 hasta el 0 de uno en uno.

Ejemplo de ejecución:

    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    0

```
#Programa3.py
```

## **3. Bucle `while`**

La idea del bucle `while` es: mientras la condición sea cierta (`True`), seguimos realizando las líneas del interior del bucle. Una vez la condición deja de ser verdadera, salimos del bucle.

Su estructura es la siguiente:

```
while condición:
  instrucción
```

Ejecución:
    instrucción 1
    instrucción 2
    .
    .
    .
    instrucción n

**Observación.** Vuelven a aparecer tanto los dos puntos después de la condición como la indentación previa a las instrucciones que se encuentran dentro del bucle.

```
i = 0 # Inicializamos la variable
while i <= 10: # Queremos que i como mucho valga 10
  print(i) # Imprimimos los números
  i += 1 # Incrementamos una unidad en cada iteración
```

## **4. Proyecto: Generador de contraseñas aleatorias**

En este proyecto tienes el deber de crear un programa que genere contraseñas aleatorias seguras para que no puedan ser hackeadas facilmente. Para ello vas a partir de 3 listas:

*   `letras`: Lista con letras mayúsculas y minúsculas
*   `digitos`: Lista con los números del 0 al 9.
*   `simbolos`: Lista con símbolos.

Tu deber es preguntar al usuario el número de letras, digitos y símbolos que quiere en su contraseña y luego generar una contraseña aleatoria.

Ejemplo de ejecución:

    Bievenido a su generador de contraseñas aleatorio

    ¿Cuantas letras quieres?: 4
    ¿Cuantos digitos quieres?: 5
    ¿Cuantos simbolos quieres?: 3
    
    Su contraseña es: aaTQ73962/&=

**Nota:** Puedes utilizar la función  [`random.choice(lista)`](https://docs.python.org/es/3/library/random.html#random.choice) para elegir elementos aleatorios de una lista.

```
import random
import string

password = ""
letras = list(string.ascii_letters)
digitos = list(string.digits)
simbolos = list(string.punctuation)

```

**Mejora final:** Haz que las letras, digitos y simbolos aparezcan en posiciones aleatorias. Puede utilizar la función [`random.shuffle(lista)`](https://docs.python.org/es/3/library/random.html#random.shuffle) que sirve para poner los elementos de una lista en posiciones aleatorias.
"""