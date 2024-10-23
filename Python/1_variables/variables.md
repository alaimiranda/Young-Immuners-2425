# **Tema 1. Trabajando con variables para manejar datos**
1. Objetivos.
2. Imprimiendo en pantalla en Python (Print).
3. Manipulación de strings.
4. Depuración en Python. (Debugging)
5. La función Input.
6. Variables en Python.
7. Nombre de las variables.
8. Proyecto: Generador de nicknames.

## **1. Objetivos**

El objetivo de este curso es que aprendas a programar como un auténtico profesional.

Utilizaremos todas las herramientas, recursos y recomendaciones que utilizan diariamente en su trabajo ingenieros de empresas tan conocidas como: Google, Meta, Netflix o la Nasa.

Para ello comenzaremos desde un nivel bajo y poco a poco iremos subiendo la dificultad. No te preocupes si los primeros temas te resultan muy fáciles ya que en muy poco tiempo estaremos haciendo proyectos alucinantes.

## **2. Imprimiendo en pantalla en Python (Print)**

La razón por la que aprendemos a programar es para poder decirle a nuestro ordenador qué necesita hacer y poder seguir nuestras instrucciones. Para ello vamos a darle nuestra primera orden al ordenador.

```
print("Alan")
```

Como se puede observar, la función print() se encarga de darle la orden al ordenador de imprimir el mensaje por pantalla. Esto quiere decir que cualquier mensaje que le pases a la función va a mostrarlo en la pantalla una vez que le das al botón de Run (ejecutar).

### **Programa 1**

Crea un programa en python que muestre la siguiente salida por consola:

```
La funcion print()
Se utiliza de la siguiente forma: 
print("Algo que imprimir")
```

## **3. Manipulación de strings**

Las cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. Podemos imaginarnos a un string como un collar en el que cada cuenta representa un espacio para una letra o símbolo.

Para crear un string hay que encerrarlo entre dobles comillas " ". Ya que esto nos identifica el inicio y el final de nuestra cadena de caracteres.

En el programa anterior hemos visto que para imprimir tres strings distintos en la consola debemos escribir tres operaciones de print(). Sin embargo, hay una manera un poco más eficiente de hacerla haciendo uso del carácter especial ‘\n’.

### **Programa 2**

Desarrolla un programa que utilizando un solo print imprima la misma salida que el programa 1.

```
La funcion print()
Se utiliza de la siguiente forma: 
print("Algo que imprimir")
```


### Concatenación

Una de las operaciones más utilizadas con strings es la concatenación. Esta consiste en unir dos o más strings utilizando el símbolo del operador suma ‘+’.

```
print("Hola" + "Immuner")
```

### **Programa 3**

Añade un espacio ' ' entre Hola e Immuner usando concatenación.

```
print("Hola" + "Immuner")
```


## **4. Depuración en Python. (Debugging)**

Depurar un programa consiste en seguir el flujo de un programa a medida que se ejecuta, de forma que podemos monitorizar qué es lo que está sucediendo en cada momento y poder corregir errores que cometemos a la hora de programar.

### **Programa 4**

Depura este programa:

```
#Programa4.py
print("Dia 1 - Manipulación de Strings.")
print("La concatenación se hace con el símbolo "+"")
print("ejemplo: print("Hello " + "world")")
print(("Los saltos de línea se crean con la barra invertida y la n")
```
Para que su salida sea la siguiente:
```
Dia 1 - Manipulación de Strings.
La concatenación se hace con el símbolo "+"
ejemplo: print("Hello " + "world")
Los saltos de línea se crean con la barra invertida y la n
```

## **5. La función Input**

La función input() es una de las funciones que vamos a estar usando constantemente. Esta te permite obtener texto escrito por teclado por parte de un usuario. Al llegar a la función, el programa se detiene esperando que se escriba algo y se pulse la tecla Enter.
```
input("¿Cómo te llamas?: ")
```
Salida:
```
¿Cómo te llamas?: Rafa
```
Si ahora escribo mi nombre y pulso Enter la línea de código donde he puesto la función input pasaría a valer Rafa para poder utilizar esa información en mi código.

### **Programa 5**

Ejecuta este programa
```
#Programa5.py
print("Hola " + input("¿Cómo te llamas?: "))
```

### **Reto 1**

Los retos son programas más difíciles que pueden que tengas que buscar información en Google o en la documentación del curso. Crear un programa que te pida tu nombre e imprima el número de caracteres que tiene.
```
#Programa6.py
```

## **6. Variables en Python**

Una variable es un espacio de la memoria de nuestro ordenador donde se guardan (y se recuperan) datos que se utilizan en un programa. Cuando escribimos código, las variables se utilizan para:

- Guardar datos y estados.
- Asignar valores de una variable a otra.
- Representar valores dentro de una expresión matemática.
- Mostrar valores por pantalla.

Tiene sentido visualizar a las variables como un teléfono apuntado en una agenda telefónica. Para ello primero debemos apuntar el nombre de la persona y luego apuntar su número de teléfono.

Esta misma operación en Python se hace de la siguiente forma:
```
#nombre_de_la_variable = valor
#nombre = teléfono
Alai = 987654321
```

Para ver más claro el uso de las variables vamos a hacer uso del siguiente programa:

```
nombre = input("¿Cómo te llamas?: ")
print(nombre)
```

### Modificar el valor de una variable

```
nombre = "Carlos"
print(nombre)
nombre = "Juana"
print(nombre)
```

También se puede imprimir un string junto a una variable utilizando el operador +.

```
nombre = "Carlos"
print("El nombre de mi amigo es: " + nombre)
```

**Nota importante:** Fíjate que cuando es un string se ponen las comillas "" para indicar que se trata de una cadena pero cuando es una variable no.

### **Reto 2**
```
#Programa7.py
a = input("a: ")
b = input("b: ")

#-----Escribe debajo de esta línea-----

#-----Escribe encima de esta línea-----

print("a = " + a)
print("b = " + b)
```

## **7. Nombre de las variables**

A la hora de nombrar a las variables podemos ponerle prácticamente el nombre que queramos. Sin embargo, es conveniente seguir unas buenas prácticas a la hora de nombrarlas para hacer nuestro código más legible.

- Se recomienda que describan su función. Ej: nombre, longitud, máximo
- Si queremos separar con guión bajo. Ej: puntuacion_usuario, fecha_maxima
- Prohibido empezar con un número. Ej: 3vidas <<---(MAL)

## **8. Proyecto: Generador de nicknames**

Por último vamos a hacer un pequeño proyecto utilizando todo lo aprendido hoy. El mío va a ser un generador de nicknames, aunque vosotros podéis ser todo lo creativos que queráis. Mi programa va a pedir el nombre de una persona, de un animal y de un lugar y va a generar un nickname de la siguiente forma:

```
#proyecto1.py
nombre = input("Nombre: ")
animal = input("animal: ")
pais = input("pais: ")

print("\n" + nombre + "_" + animal + "_" + pais )
```