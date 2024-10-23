# **Tema 2. Entendiendo los tipos de datos y fstrings.**
1. Tipos de datos primitivos en Python.
2. Función type().
3. Conversión de datos.
4. Acceder a un carácter de un string.
5. Operaciones matemáticas.
6. fStrings.
7. Manipulación de números.
8. Proyecto: Calculadora de propinas.

## **1. Tipos de datos primitivos en Python**
En el primer tema ya exploramos un tipo de dato llamado String. Sin embargo, hay muchos más tipos de datos disponibles para utilizar en Python que nos ayudan a resolver diversos problemas que serían muy complicados de hacer solo con cadenas de caracteres. Los tipos de datos que vamos a cubrir hoy son:

*   **String**: Cadenas de caracteres. “Van entre comillas”
*   **Integer**: Números enteros sin decimales. (int). 356
*   **Float**: Números con decimales. 3.14159265
*   **Boolean**: Tipo de dato que puede ser True o False. (bool)

Abre tu editor de texto para Python y escribe:
```
#Variable de tipo int.
numero = 23
#Variable de tipo string.
color = "rojo"
#Variable de tipo float.
dinero_restante = 6.7
#Variable de tipo bool.
ha_terminado = False

print(numero)
print(color)
print(dinero_restante)
print(ha_terminado)
```

## **2. Función type()**
Si en algún momento se deseara ver el tipo de dato se tendría que utilizar la función type() y entre paréntesis el dato que se quiere analizar.
```
print(type("Hola"))
print(type(33))
print(type(315.22))
print(type(True))
```

Que nos indica que “Hola” es de tipo string, 33 de tipo int, 315.22 de tipo float y True de tipo bool.

## **3. Conversión de tipos de datos**
Se van a ver tres funciones que convierten un tipo de dato en otro:
* str() ⇒ Convierte el tipo de dato en un string.
* int() ⇒ Convierte el tipo de dato en un int.
* float() ⇒ Convierte el tipo de dato en un float.

Estas funciones son muy importantes y  las iremos utilizando a lo largo de todo el año.

### **Programa 1**
```
#Programa1.py
#Explica a tu profesor qué crees que es lo que está pasando con la salida de cada tipo de datos.
print("1" + "1")
print(int("1") + int("1"))
print(float("1") + float("1"))
```

**Importante**: Si quiero recibir un número de un input() puedo lo puedo hacer de la siguiente forma:

```
edad = int(input("¿Cuántos años tienes?: "))
estatura = float(input("¿Cuánto mides?: "))
```

**Nota**: Si al ejecutarlo introduces un string() por teclado te va a dar un error de ejecución.

# **4. Acceder a un caracter de un string**
Para acceder a un carácter de un string se utiliza el operador []. Lo único muy importante que hay que tener en cuenta es que los programadores siempre empezamos a contar desde el 0 para acceder al primer carácter.
Por ejemplo en el string “Hola” podemos acceder así a todos sus caracteres:
* ‘H’ es el carácter [0].
* ‘o’ es el carácter [1].
* ‘l’ es el carácter [2].
* ‘a’ es el carácter [3].

```
print("Adios"[1])
```

### **Programa 2**
Declarar una variable de tipo string e imprime sus dos primeros caracteres por pantalla.
"""
#Programa2.py
"""

### **Programa 3. Reto**
Escribe un programa que reciba un número entero de dos dígitos utilizando la función input() y sume el valor de sus dos cifras.
Ejemplo: Si introduces el número 35 ⇒ 3 + 5 = 8.

```
#Programa3.py

```

# **5. Operaciones matemáticas**
Las operaciones matemáticas más utilizadas con números en Python son:

* + -> Suma
* - -> Resta
* * -> Multiplicación
* / -> División (Siempre devuelve un tipo float)
* // -> División entera (Siempre devuelve un tipo int)
* ** -> Potencia 

Hay que tener cuidado con los tipos de datos que vamos a operar ya que si utilizáramos el operador de resta con strings nos daría un error de tipos. También hay que tener en cuenta el orden de las operaciones. Primero potencias, después multiplicación y división, por último sumas y restas.

### **Programa 4**
Imprime por pantalla el resultado de la siguiente operación aritmética: 

```
#Programa4.py

```

El resultado debe ser 5.

# **6. fStrings**
La forma más cómoda de imprimir texto junto a variables por pantalla es mediante el uso de los fStrings.

La mayoría de veces se utilizarán dentro de la función print() de la siguiente forma:


```
nombre = input("¿Cómo te llamas?: ")
edad = int(input("¿Qué edad tienes?: "))
estatura = float(input("¿Cuánto mides?: "))

print(f"Hola soy {nombre}, tengo {edad} años y mido {estatura} m.")

```

Como se puede observar las variables hay que introducirlas dentro de llaves {}.
Nota: A partir de ahora los prints que contengan variables se realizarán de esta forma.

### **Programa 5. Reto**
En este reto crearás un programa que calcule tu vida restante en días, semanas y meses si vivieras 90 años. La ejecución del programa debe ser como la siguiente:


```
>>> Salida:
¿Qué edad tienes en años?: 25
Te quedan todavía 23725 dias, 3380 semanas y 780 meses.
```
Pistas:
* Recuerda utilizar correctamente los tipos de datos.
* Haz la salida con un fString.

Recordatorio: Puedes pedirle la edad a un usuario utilizando la siguiente línea de código:

```
edad = int(input("¿Qué edad tienes en años?: "))
```

Al final de tu código puedes tener una que te muestre el valor de las siguientes variables:

```
print(f"Te quedan todavía {dias_restantes} dias, {semanas_restantes} semanas y {meses_restantes} meses.")
```

# **7. Manipulación de números**

Cuando hablamos de números en Python nos solemos referir a datos de tipo int y float. Para estos tipos de datos hay una serie de operaciones que son muy útiles.

### **La función round()**
La función round nos retorna el número entero más cercano al que se encuentre el argumento que le pasamos entre los paréntesis.

```
#Ejemplo: Redondeo hacia arriba.
nota_obtenida = 7.8
print(f"Redondeando tienes un {round(nota_obtenida)} en el examen.")

>>> Salida:
Redondeando tienes un 8 en el examen.

#Ejemplo: Redondeo hacia abajo
latas_pintura = 6.25
print(f"Necesitas {round(latas_pintura)} latas de pintura en total.")

>>> Salida:
Necesitas 6 latas de pintura en total.

```

Esta función el problema que tiene es que no podemos decirle si queremos que redondee hacia el alza (hacia arriba) o hacia la baja, por lo que muy probablemente nos quedemos sin latas de pintura cuando estemos pintando nuestra pared.

### Más operadores
En Python, al igual que en otros lenguajes de programación existen una serie de operadores que nos permiten ahorrar tiempo cuando escribimos nuestro código.
Imagina que en un videojuego cada vez que el personaje principal consigue un punto tenemos una variable **puntuacion** que hay que ir actualizando. Para ello tenemos tres formas de hacerlo:

1ª Forma: Nunca se va a hacer así.

```
puntuacion = 0
#El personaje consigue un punto
puntuacion = 1
#El personaje consigue otro punto
puntuacion = 2
print(f"La puntuacion total es: {puntuacion}.")

>>> Salida:
La puntuacion total es: 2
```

```
puntuacion = 0
#El personaje consigue un punto (puntuacion = 1)
puntuacion = puntuacion + 1
#El personaje consigue otro punto (puntuacion = 2)
puntuacion = puntuacion + 1

print(f"La puntuacion total es: {puntuacion}.")

>>> Salida:
La puntuacion total es: 2

```

```
puntuacion = 0
#El personaje consigue un punto (puntuacion = 1)
puntuacion += 1
#El personaje consigue otro punto (puntuacion = 2)
puntuacion += 1

print(f"La puntuacion total es: {puntuacion}.")

>>> Salida:
La puntuacion total es: 2
```
# **8. Proyecto: Calculadora de propinas**
**PROYECTO FINAL:** 
Por último vas a crear una calculadora de propinas. En este programa vas a introducir la cuenta total de un restaurante, el porcentaje de propina que vais a dejar en total y el número de comensales. El programa deberá calcular el total a pagar por cada uno de los comensales.
Ejecución del programa:

```
Bienvenido al proyecto final: La calculadora de porpinas

Cuenta total: 10
Porcentaje de propina: 20
Numero de comensales: 2
Tu cuenta de 10.0 más una propina del 20.0%, es decir, 2.0 euros, se divide entre 2. Cada persona paga 6.0
```

Recomendaciones:
* La cuenta debería ser de tipo float() para poder introducir decimales.
* El porcentaje de  propina es tipo int() ya que no necesitamos decimales.
* Haz la salida por pantalla con un fString.

```
#proyecto2.py

```
