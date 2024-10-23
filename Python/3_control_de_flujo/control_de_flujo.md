# **Tema 3. Control de flujo y operadores lógicos**
1. Repaso de tipos booleanos.
2. Operadores de comparación.
3. Operadores lógicos.
4. Control de flujo con if, elif y else.
5. Proyecto: La pizzería.

## **1. Repaso de tipos booleanos**

**Dato booleano.** Es un tipo de dato que solamente puede tomar 2 valores: **`True`** (verdadero) o **`False`** (falso).

**Variable lógica.** Variable que almacena datos booleanos.
```
es_jueves = True
type(es_jueves)
```

**Nota.** Observad que tanto `True` como `False` únicamente tienen la primera letra mayúscula.

## **2. Operadores de comparación**

Estos operadores nos van a permitir hacer la comparación entre dos variables y siempre nos van a devolver un resultado de tipo **`bool`**.

Imagina que para los siguientes ejemplos tenemos declaradas dos variables enteras que valen **a = 3** y **b = 4**.

| Operador | Significado | Ejemplo |
| :---: | :--- | :--- |
| $>$ | Mayor | a > b es **False** |
| $>=$ | Mayor o igual | a >= b es **False** |
| $<$ | Menor | a < b es **True** |
| $\le$ | Menor o igual | a <= b es **True** |
| $==$ | Igual | a == b es **False** |
| $!=$ | Distinto | a != b es **True** |

**Observación**: Nota como el operador == es de comparación mientras que el operador = es de asignación.

### **Programa 1:**

Completa el programa para que su salida por pantalla sea la siguiente:
```
    a > b: False
    a >= b: False
    a < b: True
    a <= b: True
    a == b: False
    a != b: True
```
```
#Programa1.py
a = 3
b = 4

print(f"a > b: {a > b}")
```

## **3. Operadores lógicos**

Los operadores lógicos que se pueden utilizar en Python son: **`and`**, **`or`** y **`not`**.

Imagina que para los siguientes ejemplos tenemos declaradas dos variables tipo bool que valen **x = True** y **y = False**.

| Operador | Significado | Ejemplo |
| :---: | :--- | :--- |
| and | True si los dos operandos son True | x and y es **False** |
| or | True si uno de los operandos es True | x or y es **True** |
| not | True si el operando es False (complemento) | not y es **True** |


### **Programa 2:**

Completa el programa para que su salida por pantalla sea la siguiente:
```
    x and y: False
    x or y: True
    not x: False
    not y: True
```
```
#Programa2.py
x = True
y = False

print(not y)
```

## **4. Control de flujo con if, elif y else**

### **if**

Cuando queremos comprobar si se cumple alguna condición, utilizamos el operador de decisión `if`. La sintaxis que debemos seguir es la siguiente:

```
if condicion:
    consecuencia
    consecuencia
    consecuencia

```

**¡Cuidado!** La sintaxis de los dos puntos después de la condición y la indentación (equivalente a una tabulación, un total de 4 espacios en blanco) que precede a la consecuencia es muy importante. De hecho, si se omite alguna de las dos cosas o bien nos pasamos de indentación, nos saltará error.

- Si queréis hacer una tabulación, debéis pulsar el tabulador una vez.
- Podéis hacer tabulaciones en bloque seleccionando las líneas de código que queráis indentar y, a continuación, pulsando el tabulador.
- Podéis deshacer tabulaciones pulsando Shift + Tab
- Podéis deshacer tabulaciones en bloque seleccionando las líneas de código que queráis desindentar y, a continuación, pulsando el Shift + Tab.

### Ejemplo:

Si el usuario introduce una edad entre 8 y 18 años podrá formar parte de Young Immuners.
```
edad = int(input("¿Que edad tienes?: "))
if (edad >= 8 and edad <= 18):
    print("Puedes formar parte de Young Immuners")
```

### **else**

Ahora, nos podríamos preguntar qué le podríamos decir al usuario en el caso en que no satisfaga la condición. Ahí es donde entra en juego el operador de decisión `else`. Esta vez, la sintaxis a seguir es la siguiente:

```
if condición:
    consecuencia_si_es_verdad
else:
    consecuencia_si_es_falsa

```

Siguiendo el ejemplo anterior, si el usuario tiene 8 años o más, pero menos de 18, entonces puede formar parte de Young Immuners. Si no, le diremos que no satisface una necesidad básica para ser miembro.

```
edad = int(input("¿Que edad tienes?: "))
if edad >= 8 and edad <= 18:
    print("Puedes formar parte de Young Immuners")
else:
    print("No puedes formar parte de Young Immuners")
```

### **elif**

Ahora, en vez de comprobar si se cumple o no una condición, nos podríamos preguntar cómo haríamos para comprobar más de una condición. Para ello se suele utilizar el operador de decisión `elif`.

El operador `elif` funciona del siguiente modo: se empieza con un operador `if`; si la condición de este no se cumple, pasamos a la siguiente condición posible precedida de un `elif`; si esta tampoco se cumple, pasamos al siguiente `elif`; seguimos así hasta que o bien se satisface alguna condición y realizamos su consecuencia, o hasta llegar al `else`, que implica que no se ha satisfecho ninguna de las condiciones anteriores.

La sintaxis del operador de decisión `elif` es la siguiente:

```
if condición_1:
  consecuencia
elif condición_2:
  consecuencia
elif condición_3:
  consecuencia
.
.
.
else:
  consecuencia
```

Recuperemos el ejemplo que debemos tener entre 8 y 18 años para formar parte de Young Immuners.

```
edad = int(input("¿Que edad tienes?: "))
if edad > 18:
    print("Ya eres muy mayor para apuntarte a Young Immuners")
elif edad >= 8:
    print("¡Puedes apuntarte a Young Immuners!")
else:
    print("Eres muy pequeño para apuntarte a Young Immuners")
```

El funcionamiento del código anterior es el siguiente:

- El `if` comprueba si la edad introducida es mayor a 18.
- El `elif` comprueba si la edad se encuentra en el intervalo [8, 18]
- El `else` implica que la edad introducida es menor a 8

### **Programa 3 - Reto:**

Crea un programa que le pida al usuario un número y le diga a este si es par o impar.

Ejemplos de ejecución:
```
    Introduce un numero: 7
    El numero 7 es impar.
```
---
```
    Introduce un numero: 2
    El numero 2 es par.
```

**Nota**: Puede que necesites buscar el uso del operador %. [Link operadores Python](https://ellibrodepython.com/operadores-aritmeticos#operador--3)

```
#Programa3.py
```

## 5. Proyecto: La pizzería

En este proyecto vas a ser el encargado de tomar las comandas de los clientes de una pizzería y de entregar la cuenta a los clientes. Para ello utilizarás uso de variables, fstrings, operadores lógicos...

Precios del menú:

*   Pizza pequeña: 5€
*   Pizza mediana: 8€
*   Pizza grande: 11€
*   Extra de queso: +1€
*   Extra de pepperoni: +2€

Ejemplo de ejecución:
---
    ¿De que tamaño quieres la pizza? 'p', 'm' o 'g'?: g
    ¿Desea extra de queso?: 's' o 'n': n
    ¿Desea extra de pepperoni?: 's' o 'n': s
    La cuenta es: 13€.

```
#Proyecto3.py
```