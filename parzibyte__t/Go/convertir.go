package main

import "fmt"

func main() {
	idUsuario:= session.values["idUsuario"] // Es una interface
	idUsuarioEntero, ok:= idUsuario.(int64)
	if ok {

	} else {
		fmt.Println("Error, no se pudo convertir a int64")
	}
}