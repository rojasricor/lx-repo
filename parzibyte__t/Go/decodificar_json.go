package main

/**
 * Decodificar JSON con Go
 * @author parzibyte
 */
import (
	"encoding/json"
	"fmt"
)

func main() {
	// Nota: Convertimos a []byte la cadena porque Unmarshal lo pide

	nombreComoJson := []byte(`"Luis Cabrera Benito"`)
	// Definir variable
	var nombre string
	// Decodificar. No olvides pasar LA DIRECCIÓN en lugar de la variable en sí
	err := json.Unmarshal(nombreComoJson, &nombre)
	if err != nil {
		fmt.Printf("Error decodificando: %v\n", err.Error())
	} else {
		fmt.Printf("Nombre: %s\n", nombre)
	}

	// Arreglo como JSON, este podría venir de un formulario, petición o lo que sea

	arregloComoJson := []byte(`["Resident Evil","Super Mario Bros","Cuphead","Halo"]`)
	// Debemos definir la variable que alojará los valores decodificados
	arreglo := []string{}
	// Y ahora decodificamos pasando el apuntador
	err = json.Unmarshal(arregloComoJson, &arreglo)
	if err != nil {
		fmt.Printf("Error decodificando: %v\n", err)
	} else {
		fmt.Println("En posición 0: ", arreglo[0]) // Resident Evil
	}

	// Otra vez los structs
	type Raza struct {
		Nombre, Pais string
	}

	type Mascota struct {
		Nombre string
		Edad   int
		Raza   Raza
		Amigos []string // Arreglo de strings
	}

	// Vamos a probar...
	mascotaComoJson := []byte(`{"Nombre":"Maggie","Edad":3,"Raza":{"Nombre":"Caniche","Pais":"Francia"},"Amigos":["Bichi","Snowball","Coqueta","Cuco","Golondrino"]}`)

	// Recuerda, primero se define la variable
	var mascota Mascota

	// Y luego se manda su dirección de memoria
	err = json.Unmarshal(mascotaComoJson, &mascota)
	if err != nil {
		fmt.Printf("Error decodificando: %v\n", err)
	} else {
		// Listo. Ahora podemos imprimir
		fmt.Printf("El nombre: %s\n", mascota.Nombre)
		fmt.Printf("País de Raza: %s\n", mascota.Raza.Pais)
		fmt.Printf("Primer amigo: %v\n", mascota.Amigos[0])
	}
}