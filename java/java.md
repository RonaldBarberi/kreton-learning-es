# Java

## VARIABLES Y CONSTANTES

Una variable es un nombre que se asocia con una porción de la memoria de la computadora, en la que se guarda un valor determinado.

Tipos de datos:
- Entero => int => Ej: 0, 2, 4, 8, 16, 32, 64, 128, etc
- Decimales => double => Ej: 1,5; 1,8; 67,99; etc
- Booleanos => Boolean => true o false
- Caracteres => char => 'a', 'b', 'c', 'd', etc
- Cadenas de Caracteres/Texto => String => "Bienvenido con KretoN"
- Entero Largo => long => números entre: (-9.223.372.036.854.775.808 y 9.223.372.036.854.775.807)

Para declarar una variable se hace de la siguiente forma:

Primero debe ir el Tipo de Datos seguido del nombre de la variable 
Ej:
```java
// Declaranto variables
String myTexto = "Hola, soy KretoN";
System.out.println(myTexto);
```

---

## OPERADORES ARITMÉTICOS

Un operador es un simbolo especial que indica al compilador que debe efectuar una determinada operación.

- Ariméticos:
   - "+"
   - "-"
   - "*"
   - "/"

- Relacionales
   - "=="
   - ">, <"
   - ">=, <="
   - "!="

- Condicionales
   - "&& (AND o Y)"
   - "|| (OR u O)"
   - "! (NOT o negación)"

```java
// Realizando operaciones Artimeticas
int num1, num2, result;

num1 = 4;
num2 = 2;

result = num1 * num2;
System.out.println("El resultado es: " + result);
```

---

## Condicional IF en Java

La condicional IF es utilizada para realizar una prueba logica y así retornar un valor True o False, ese valor True o False pueden ser especificados para que realice una acción especificada. Puediendo utilizar el IF, IFELSE y ELSE.

```java
// Condicional IF en Java
int dineroCuenta = 25000;
int valorCoche = 27000;

if (dineroCuenta >= valorCoche) {
    System.out.println("Puedes comprar el Carro y te sobran"+ (dineroCuenta - valorCoche));
}


// If con ElSE
if (dineroCuenta >= valorCoche) {
    System.out.println("Puedes comprar el Carro y te sobran"+ (dineroCuenta - valorCoche));
}
else {
    System.out.println("No puedes comprar el Carro y te faltan: "+ (valorCoche - dineroCuenta) + " dolares.");
}


// If con IFELSE y ElSE
if (valorCoche > dineroCuenta) {
    saldoConPrestamo += prestamoBanco; 
}

if (saldoConPrestamo >= valorCoche) {
    System.out.println("Puedes comprar el Carro y te sobran " + (saldoConPrestamo - valorCoche) + " dolares.");
}
else {
    if (valorCoche > saldoConPrestamo) {
        System.out.println("No puedes comprar el Carro y te faltan" + (valorCoche - saldoConPrestamo));
    }
}
```

---

## CONDICIONAL SWITCH

La estructura "Switch" permite múltiples caminos a partir de la evaluación de una sola experesión/condición.

```java
// Condicional Switch
int diaCitaMedica = 4;
String nombreDia;

switch (diaCitaMedica) {
    case 1: nombreDia="Lunes";
    break;
    case 2: nombreDia="Martes";
    break;
    case 3: nombreDia="Miercoles";
    break;
    case 4: nombreDia="Jueves";
    break;
    case 5: nombreDia="Viernes";
    break;
    case 6: nombreDia="Sabado";
    break;
    case 7: nombreDia="Domingo";
    break;
    default: nombreDia="Numero de dia es invalido";
}

System.out.println("El dia de la semana seleccionado es: "+ nombreDia);
```

---

## OPERADOR TERNARIO

El Operador Tenario es una herramienta en Java para tomar decisiones simples en una sola línea de código, no como el IF que permite escalar.

```java
// Operador Ternario
int notaEstudiante = 29;

String aprueba = (notaEstudiante >= 30) ? "Aprueba" : "Reprobado";
System.out.println(aprueba);
```

---

## WHILE

Permite ejecutar una cantidad de veces en ciclo un comando conforme a un criterio. Ya sean controlados por un contador o por un centinela.

```java
// WHILE
int contador = 0;

while (contador < 5) {
    System.out.println("Aún es menor a 5.");
    contador = contador + 1;
}
```

---

## FOR

El bucle for realiza una determinada cantidad de veces. Se le puede considerar un bucle controlado por contador; sin embargo posee su variable contadora propia.

```java
// FOR
String[] nombreAlumnos = {"Ronald", "Ana", "Junior"};

for (int i = 0; i < nombreAlumnos.length; i++) {
    System.out.println(nombreAlumnos[i]);
}
```

---

## ARRAYS (VECTORES Y MATRICES)

Los arrays son un conjunto de de datos que se almacenan en memoria de manera continua con el mismo nombre pero con diferentes indices para interactuar entre ellos.

```java
// ARRAY
int vector[] = new int [4];

vector[1] = 2;
vector[2] = 6;
vector[3] = 13;

for (int i = 0; i < vector.length; i++) {
    System.out.println(vector[i]);
}
```

---

## 