package main

/**
 * Codificar a JSON con Go
 * @author parzibyte
 */
import (
	"encoding/json"
	"fmt"
)

func main() {
	// Cadenas
	nombre := "Luis Cabrera Benito"
	nombreComoJson, err := json.Marshal(nombre)
	if err != nil {
		fmt.Printf("Error codificando nombre: %v", err)
	} else {
		fmt.Println(string(nombreComoJson))
	}

	// Números
	edad := 21
	edadComoJson, err := json.Marshal(edad)
	if err != nil {
		fmt.Printf("Error codificando edad: %v", err)
	} else {
		fmt.Println(string(edadComoJson))
	}

	// Arreglos de todo tipo. En este caso de cadena...
	videojuegos := []string{"Resident Evil", "Super Mario Bros", "Cuphead", "Halo"}
	videojuegosComoJson, err := json.Marshal(videojuegos)
	if err != nil {
		fmt.Printf("Error codificando videojuegos: %v", err)
	} else {
		fmt.Println(string(videojuegosComoJson))
	}

	// Structs. Definimos unos para ver que soporta profundidad

	type Raza struct {
		Nombre, Pais string
	}

	type Mascota struct {
		Nombre string
		Edad   int
		Raza   Raza
		Amigos []string // Arreglo de strings
	}

	// Creamos algunos y los codificamos
	raza := Raza{"Caniche", "Francia"}
	amigos := []string{"Bichi", "Snowball", "Coqueta", "Cuco", "Golondrino"}
	mascota := Mascota{"Maggie", 3, raza, amigos}
	mascotaComoJson, err := json.Marshal(mascota)
	if err != nil {
		fmt.Printf("Error codificando mascota: %v", err)
	} else {
		fmt.Println(string(mascotaComoJson))
	}
}
