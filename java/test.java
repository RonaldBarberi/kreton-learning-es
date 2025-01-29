import java.util.Scanner;

public class test {

    public static void main(String[] args) {
        
        // Declaranto variables
        String myTexto = "Hola, soy KretoN";
        System.out.println(myTexto);
        
        
        // Realizando operaciones Artimeticas
        int num1, num2, result;
        
        num1 = 4;
        num2 = 2;
        
        result = num1 * num2;
        System.out.println("El resultado es: " + result);
        

        // Ejecricio de Intercambios de valores en Java
        int numero, numero2, numTemp;
        
        numero = 32;
        numero2 = 20;
        
        numTemp = numero;
        numero = numero2;
        numero2 = numTemp;        
        System.out.println("Numero es: " + numero + " Y número2 es: " + numero2);
        
        
        // Condicional IF en Java
        int dineroCuenta = 25000;
        int valorCoche = 27000;
        int prestamoBanco = 3000;
        int saldoConPrestamo = dineroCuenta;
        
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
        
        

        // Ejecicio:
        float salarioRepositor = 15890f;
        float salarioCajero = 25630f;
        float salarioSupervisor = 35560f;
        float salarioTotal = 0f;
        Scanner textInput = new Scanner(System.in);
        
        String[] opcionCargos = {
            "Repositor",
            "Cajero",
            "Supervisor"
        };

        System.out.println("Seleccione un cargo de la lista:");
        for (int i = 0; i < opcionCargos.length; i++) {
            System.out.println((i + 1) + ". " + opcionCargos[i]);
        }

        System.out.print("Ingresa el número de la opción: ");
        int option = textInput.nextInt();
        
        if (option < 1 || option > opcionCargos.length) {
            System.out.print("Opción inválida. Debes elegir un número entre 1 y " + opcionCargos.length);
        }
    
        String cargoEmpleado = opcionCargos[option - 1];

        switch (option) {
            case 1: salarioTotal = salarioRepositor + (salarioRepositor * 0.10f);
            break;
            case 2: salarioTotal = salarioCajero;
            break;
            case 3: salarioTotal = salarioSupervisor + (salarioSupervisor * 0.11f);
            break;
            default: salarioTotal=0;
        }
        if (salarioTotal == 0) {
            System.out.println("No se a podido calcular el dalario total debido a que el cargo digitado es erroneo: " + cargoEmpleado);
        }
        else {
            System.out.println("El salario total para el cargo "+ cargoEmpleado+ "es de "+ salarioTotal);
        }


        // Operador Ternario
        int notaEstudiante = 29;

        String aprueba = (notaEstudiante >= 30) ? "Aprueba" : "Reprobado";
        System.out.println(aprueba);


        // WHILE
        int contador = 0;

        while (contador < 5) {
            System.out.println("Aún es menor a 5.");
            contador = contador + 1;
        }


        // FOR
        String[] nombreAlumnos = {"Ronald", "Ana", "Junior"};

        for (int i = 0; i < nombreAlumnos.length; i++) {
            System.out.println(nombreAlumnos[i]);
        }


    }
    
}