package main

import (
	"fmt"
	"strconv"
)

func CadenaToInt() {
	numeroCadena := "15"
	numeroEntero, error := strconv.Atoi(numeroCadena)
	if error != nil {
		fmt.Println("Error al convertir: ", error)
	}
	fmt.Println(numeroEntero + 5)
}

func IntToCadena() {
	// fmt.Println("Hola" + strconv.Itoa(23))
	Numero := 928782382
	cad := strconv.Itoa(Numero)
	fmt.Println(cad + "")
}

func IntToBinario() {
	numero := int64(20)
	bin := strconv.FormatInt(numero, 2)
	fmt.Printf("El numero original es: %d, but the binary number is: %s", numero, bin)
	fmt.Println()
}

func BinarioToInt() {
	binario := "10101101001"
	entero, e := strconv.ParseInt(binario, 2, 64)

	if e != nil {
		fmt.Println("Error al convertir :( ", e)
	} else {
		fmt.Printf("El número binario %s es %d en su representación decimal", binario, entero)
	}
	fmt.Println()
}

func main() {
	BinarioToInt()
}
