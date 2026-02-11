package sebastianquiroga;

public class SebastianQuiroga {

    // Objeto que contiene correo e ID
    static class DatosEstudiante {
        String correo;
        String id;

        DatosEstudiante(String correo, String id) {
            this.correo = correo;
            this.id = id;
        }

        void imprimirDatos() {
            System.out.println("Correo: " + correo);
            System.out.println("ID: " + id);
        }
    }

    public static void main(String[] args) {

        System.out.println(" TRABAJO INDIVIDUAL - CONCEPTOS FUNDAMENTALES ");

        /* las 
         4 variables 
          diferentes */

        int edad = 20;                 // tipo entero
        double promedio = 4.5;         // tipo decimal
        char grupo = 'A';              // tipo carácter
        boolean activo = true;         // tipo lógico

        System.out.println("VARIABLES DE DIFERENTES TIPOS:");
        System.out.println("Edad (int): " + edad);
        System.out.println("Promedio (double): " + promedio);
        System.out.println("Grupo (char): " + grupo);
        System.out.println("Activo (boolean): " + activo + "\n");

        System.out.println("ESTRUCTURAS DE DATOS");
        System.out.println("Sirven para organizar y almacenar información de manera eficiente.");
        System.out.println("En otras palabras elegir bien una estructura de datos mejora el rendimiento del programa.\n");

        System.out.println("PROGRAMACIÓN LINEAL");
        System.out.println("Se utiliza para resolver problemas de optimización con restricciones.");
        System.out.println("En otras palabras ayuda a tomar decisiones óptimas usando modelos matemáticos.\n");

        System.out.println("ALGORITMOS VORACES");
        System.out.println("Toman la mejor decisión inmediata en cada paso.");
        System.out.println("En otras palabras son rápidos y fáciles de implementar en problemas adecuados.\n");

        System.out.println("TDA GRAFOS");
        System.out.println("Representan relaciones entre elementos mediante nodos y aristas.");
        System.out.println("En otras palabras permiten modelar redes y conexiones del mundo real.\n");

        System.out.println("TDA ÁRBOLES");
        System.out.println("Organizan información de forma jerárquica.");
        System.out.println("En otras palabras facilitan búsquedas rápidas y ordenadas.\n");

        System.out.println("REFERENCIAS:");
        System.out.println("Cormen et al. (2009). Introduction to Algorithms. MIT Press.");
        System.out.println("Sedgewick & Wayne (2011). Algorithms. Addison-Wesley.");
        System.out.println("Taha (2017). Operations Research: An Introduction. Pearson.\n");

        System.out.println("DATOS DEL ESTUDIANTE");
        System.out.println("Nombre: Sebastian Quiroga");

        DatosEstudiante estudiante = new DatosEstudiante(
            "squiroga585@unab.edu.co",
            "U00168822"
        );

        estudiante.imprimirDatos();
    }
}
