/*
    https://parzibyte.me/blog
*/
#include <stdio.h>
#include <string.h>
#include <math.h>

#define MAXIMA_LONGITUD_CADENA 100

void invertirCadena(char cadena[])
{
    int longitud = strlen(cadena);
    int i;
    for (i = 0; i < strlen(cadena) / 2; i++)
    {
        char temporal = cadena[i];
        cadena[i] = cadena[longitud - i - 1];
        cadena[longitud - i - 1] = temporal;
    }
}

void concatenarCharACadena(char c, char *cadena)
{
    char cadenaTemporal[2];
    cadenaTemporal[0] = c;
    cadenaTemporal[1] = '\0';
    strcat(cadena, cadenaTemporal);
}

/**
 * Convierte un número decimal a cualquier base
 * @param numeroDecimal El número en base 10
 * @param cadenaResultado Cadena en donde se almacenará el resultado, pues esta función no devuelve nada, solo coloca el resultado en la cadena indicada
 * @param base La base a la que se desea convertir el número. Por ejemplo, para convertir a hexadecimal, la base es 16
 * @param digitos Los dígitos que conforman la base a la que se convierte el número. Por ejemplo, para la base 16 son 0123456798ABCDEF
 * @author Parzibyte https://parzibyte.me/blog
 */
void decimalACualquierBase(double numeroDecimal, char cadenaResultado[MAXIMA_LONGITUD_CADENA], const int base, const char digitos[])
{
    /*
     * Separar fracción y entero
     * */
    double parteEnteraDouble; // Temporal para modf
    double parteFraccionaria;
    parteFraccionaria = modf(numeroDecimal, &parteEnteraDouble);
    int parteEntera = (int)parteEnteraDouble;
    /*
     * Declarar cadenas
     * */
    char cadenaParteEntera[MAXIMA_LONGITUD_CADENA] = "";
    char cadenaParteFraccionaria[MAXIMA_LONGITUD_CADENA] = "";
    // Realizar la conversión de la parte entera
    while (parteEntera > 0)
    {
        int residuo = parteEntera % base;
        char digito = digitos[residuo];
        concatenarCharACadena(digito, cadenaParteEntera);
        parteEntera /= base;
    }
    // Invertimos la cadena
    invertirCadena(cadenaParteEntera);
    // Realizar conversión de la parte fraccionaria
    double sobrante;
    do
    {
        double resultado = parteFraccionaria * base;
        parteFraccionaria = modf(resultado, &sobrante);
        char digito = digitos[(int)sobrante];
        concatenarCharACadena(digito, cadenaParteFraccionaria);
    } while (sobrante != 0);
    // Concatenar finalmente la parte entera y fraccionaria en el resultado
    strcpy(cadenaResultado, ""); // Limpiar cadena
    strcat(cadenaResultado, cadenaParteEntera);
    strcat(cadenaResultado, ".");
    strcat(cadenaResultado, cadenaParteFraccionaria);
}

int main(int argc, char const *argv[])
{
    // En dónde almacenar el resultado, debe ser una cadena
    char resultado[MAXIMA_LONGITUD_CADENA] = "";
    // Solicitar número al usuario;
    double decimal;
    printf("Ingresa el decimal:\n");
    scanf("%lf", &decimal);
    // Decimal a hexadecimal
    decimalACualquierBase(decimal, resultado, 16, "0123456789ABCDEF");
    printf("Resultado de convertir el decimal %lf a hexadecimal: %s\n", decimal, resultado);
    // Decimal a octal
    decimalACualquierBase(decimal, resultado, 8, "01234567");
    printf("Resultado de convertir el decimal %lf a octal: %s\n", decimal, resultado);
    // Decimal a binario
    decimalACualquierBase(decimal, resultado, 2, "01");
    printf("Resultado de convertir el decimal %lf a binario: %s\n", decimal, resultado);
    return 0;
}