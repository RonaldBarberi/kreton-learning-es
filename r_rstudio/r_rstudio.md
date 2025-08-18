# R - R Studio

## VARIABLES Y CONSTANTES

Una variable es un nombre que se asocia con una porción de la memoria de la computadora, en la que se guarda un valor determinado.

Tipos de datos:
- Entero => int => Ej: 10L
- Decimales => double => Ej: 3.14
- Booleanos => Boolean => TRUE o FALSE
- Caracteres => char => 'a', 'b', 'c', 'd', etc
- Cadenas de Caracteres/Texto => String => "Bienvenido con KretoN"
- Entero Largo => as.integer64("9223372036854775807")

Para declarar una variable se hace de la siguiente forma:

Primero debe ir el Tipo de Datos seguido del nombre de la variable 
Ej:
```R
# Declaranto variables
variable_texto = "Hola, soy KretoN"
print(variable_texto)
```

---

## OPERADORES ARITMÉTICOS

Un operador es un simbolo especial que indica al compilador que debe efectuar una determinada operación.

- Ariméticos:
   - "+" - Suma
   - "-" - Resta
   - "*" - Multiplicación
   - "/" - División
   - "^ o **" - Potencia
   - "%%" - Módulo (Resto de división)
   - "%/%" - División entera (cociente sin decimales)

- Relacionales
   - "==" - Igual a
   - ">, <" - Mayor, menor qué
   - ">=, <=" - Mayor, menor igual qué
   - "!=" - Distinto de

- Condicionales
   - "&" - AND (elemento a elemento)
   - "&&" AND (solo primer elemento)
   - "|" OR (elemento a elemento)
   - "||" OR (solo primer elemento)
   - "!" NOT (negación)

```R
# Realizando operaciones Artimeticas
num1 = 4
num2 = 2

result = num1 * num2
cat("El resultado es:", result)
```

---

## Condicional IF en R

La condicional IF es utilizada para realizar una prueba logica y así retornar un valor True o False, ese valor True o False pueden ser especificados para que realice una acción especificada. Puediendo utilizar el IF, IFELSE y ELSE.

```R
# Condicional IF en R
dinero_cuenta <- 25000
valor_coche <- 27000
saldoConPrestamo <- dinero_cuenta
prestamoBanco <- 5000

# IF simple
if (dinero_cuenta >= valor_coche) {
  cat("Puedes comprar el Carro y te sobran", dinero_cuenta - valor_coche, "dólares.\n")
}

# IF con ELSE
if (dinero_cuenta >= valor_coche) {
  cat("Puedes comprar el Carro y te sobran", dinero_cuenta - valor_coche, "dólares.\n")
} else {
  cat("No puedes comprar el Carro y te faltan", valor_coche - dinero_cuenta, "dólares.\n")
}

# IF con ELSE IF y ELSE
if (valor_coche > dinero_cuenta) {
  saldoConPrestamo = saldoConPrestamo + prestamoBanco
}

if (saldoConPrestamo >= valor_coche) {
  cat("Puedes comprar el Carro y te sobran", saldoConPrestamo - valor_coche, "dólares.\n")
} else if (valor_coche > saldoConPrestamo) {
  cat("No puedes comprar el Carro y te faltan", valor_coche - saldoConPrestamo, "dólares.\n")
}
```

---

## CONDICIONAL SWITCH

La estructura "Switch" permite múltiples caminos a partir de la evaluación de una sola experesión/condición.

```java
// Condicional Switch
color = "rojo"

mensaje = switch(color,
                  "rojo" = "El color es rojo",
                  "azul" = "El color es azul",
                  "verde" = "El color es verde",
                  "Color no reconocido"
                )

print(mensaje)


opcion = 3

mensaje = switch(opcion,
                  "Has elegido sumar",
                  "Has elegido restar",
                  "Has elegido multiplicar",
                  "Has elegido dividir",
                  "Opción inválida"
                )

cat(mensaje, "\n")

```

---

## OPERADOR TERNARIO

El Operador Tenario es una herramienta en Java para tomar decisiones simples en una sola línea de código, no como el IF que permite escalar.

```R
# Operador Ternario

x = 10
resultado = ifelse(x > 5, "Mayor que 5", "Menor o igual a 5")
print(resultado)
```

---

## WHILE

Permite ejecutar una cantidad de veces en ciclo un comando conforme a un criterio. Ya sean controlados por un contador o por un centinela.

```R
// WHILE
suma = 0
num = 1

while (num <= 10) {
  suma = suma + num
  num = num + 1
}

cat("La suma de 1 a 10 es:", suma, "\n")
```

---

## FOR

El bucle for realiza una determinada cantidad de veces. Se le puede considerar un bucle controlado por contador; sin embargo posee su variable contadora propia.

```R
// FOR
nombres = c("Ana", "Luis", "Carlos")

for (nombre in nombres) {
  cat("Hola", nombre, "\n")
}
```

---

## ARRAYS (VECTORES Y MATRICES)

Los arrays son un conjunto de de datos que se almacenan en memoria de manera continua con el mismo nombre pero con diferentes indices para interactuar entre ellos.

```R
// ARRAY
# Crear un vector de 4 elementos inicializados en 0
vector <- numeric(4)

# Asignar valores (¡Ojo! en R los índices empiezan en 1, no en 0 como en Java)
vector[2] <- 2
vector[3] <- 6
vector[4] <- 13

# Recorrer con for
for (i in 1:length(vector)) {
  cat("Elemento", i, ":", vector[i], "\n")
}
```

---
