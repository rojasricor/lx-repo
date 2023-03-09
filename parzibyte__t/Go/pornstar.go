package main

import "fmt"

type Persona struct {
	fullname string
	age, cmPENE int
}

type Pornstar struct {
	name, lastname string
	age            int
	sana           bool
	word1          string
	word2          string
	gemidos        string
	duenio Persona
}

func (xxx *Pornstar) follarmeARicardo() {
	fmt.Printf("%s %s meteme tu verga de %d centimetros!!!", xxx.gemidos, xxx.duenio.fullname, xxx.duenio.cmPENE)
}

func (xxx *Pornstar) tenerSexo() {
	fmt.Printf("%s que %s papi metemelo mas %s", xxx.gemidos, xxx.word1, xxx.word2)
}

func (xxx *Pornstar) Name() string {
	return xxx.name
}

func (xxx *Pornstar) setSana(newSana bool) {
	xxx.sana = newSana
}

func main() {
	Culiador := Persona{"Ricardo Andres Rojas Rico", 18, 20}
	LanaRhoades := Pornstar{"Lana", "Rhoades", 22, true, "Oh my god!", "rico", "Ahhh!!! Ahh! Ah!", Culiador}
	MiaKhalifa := Pornstar{
		age:      28,
		name:     "Mia",
		lastname: "Khalifa",
		sana:     false,
		word1: "papi",
		word2: "duro",
		gemidos: "Ahhh!!! Ahh! Ah!",
		duenio: Culiador,
	}
	fmt.Println(LanaRhoades)
	fmt.Println(MiaKhalifa)

	LanaRhoades.tenerSexo()
	MiaKhalifa.tenerSexo()

	/**
	 * Modificar sus gemidos y luego tener sexo otra vez
	 */
	LanaRhoades.gemidos = "Ah oh my god ahhhhhhhhhhhhhhhh!"
	LanaRhoades.word1 = "duro"
	LanaRhoades.tenerSexo()

	fmt.Println()

	gemidosDeLanaRhoades := LanaRhoades.gemidos
	fmt.Println("Lana Rhoades: ", gemidosDeLanaRhoades)

	fmt.Println()

	fmt.Println(LanaRhoades.Name())

	MiaKhalifa.setSana(true)
	fmt.Println(MiaKhalifa)

	LanaRhoades.follarmeARicardo()


}
