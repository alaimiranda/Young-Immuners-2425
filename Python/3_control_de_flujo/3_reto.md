# 🧩 Reto: Adivina el Número

## Descripción:
Crea un programa que permita al usuario adivinar un número entre 1 y 100. El programa le dirá al usuario si el número es correcto o incorrecto. Tendrá 3 intentos para adivinar.

## Instrucciones:
1. El programa generará un número aleatorio entre 1 y 100.
2. Pedirá al usuario que adivine el número.
3. Si el número es correcto, mostrará un mensaje de felicitaciones.
4. Si es incorrecto, el programa indicará si el número es mayor o menor y permitirá otro intento.
5. El usuario tiene un total de 3 intentos para adivinar el número.
6. Si no lo adivina después de 3 intentos, el programa revelará el número correcto.

## Ejemplo de ejecución:
´´´
Adivina el número entre 1 y 100: 50
Incorrecto. El número es mayor.
Adivina el número entre 1 y 100: 90
¡Correcto! El número era 90.
´´´

### Pistas:
- Puedes usar el módulo random de Python para generar el número aleatorio.
- Usa estructuras de control como if, elif, else para verificar si el número es correcto o incorrecto.
- Usa un ciclo while para los intentos del usuario.