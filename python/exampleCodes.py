# def puedePasarParaMontaniaRusa():
# 	nombre = input('Como te llamas? ')
# 	print(f'Hola {nombre}')
# 	edad = int(input('Cuantos anios tienes? '))
# 	masDe12 = edad>=12
# 	respuestaHijoDelDuenio = input('Es hijo del dueno? ')
# 	esHijoDelDuenio =respuestaHijoDelDuenio == 'si'
# 	puedePasar = masDe12 or esHijoDelDuenio
# 	if puedePasar:
# 		print('Usted puede pasar a la montania rusa')
# 	else:
# 		print('No puede pasar :(')
# puedePasarParaMontaniaRusa()

# def mostrarPrecioFinal(producto, precio, descuento):
# 	precioFinal = precio - descuento * precio / 100
# 	print(f"El precio del {producto} es ${precioFinal}")
# mostrarPrecioFinal('Pantalon', 40, 20)
# mostrarPrecioFinal('Cinturon', 284, 20)

# def calcularIMC():
# 	peso = float(input('ingrese su peso en kg: '))
# 	alturaEnCm = int(input('ingrese su altura en cm: '))
# 	alturaEnMetros = alturaEnCm / 100
# 	imc = peso / (alturaEnMetros**2)
# 	print(f'Su IMC es de {imc}')
# 	if imc<20:
# 		return('Estado de delgadez')
# 	if imc>=20 and imc<26:
# 		return('Peso normal')
# 	if imc>=26 and imc<30:
# 		return('Estado de sobrepeso')
# 	if imc>=30:
# 		return('Estado de obesidad')
# print(calcularIMC())

# def chatear():
# 	def chat(texto):
# 		texto = texto.replace(':)', '😀')
# 		texto = texto.replace(':{', '😠')
# 		texto = texto.replace(':|', '😑')
# 		texto = texto.replace(':(', '😥')
# 		texto = texto.replace(':*', '😗')
# 		texto = texto.replace(':/', '🫤')
# 		return texto
# 	texto = input('> ')
# 	while texto != 'quit':
# 		print(chat(texto))
# 		texto = input('> ')
# chatear()

# numeros = {
# 	'1': 'uno',
# 	'2': 'dos',
# 	'3': 'tres',
# 	'4': 'cuatro',
# 	'5': 'cinco',
# 	'6': 'seis',
# 	'7': 'siete',
# 	'8': 'ocho',
# 	'9': 'nueve',
# }
# def letterNumbers(number):
# 	cad = ''
# 	for n in number:
# 		cad += numeros[n] + ' '
# 	return cad
# number = input('numero > ')
# print(letterNumbers(number))

def encriptar(texto):
	print(f'El texto a encriptar es {texto}')
	finalText = ''
	for letra in texto:
		ascii = ord(letra)
		ascii+=1
		finalText += chr(ascii)
	return finalText

def desencriptar(texto):
	print(f'El texto a desencriptar es {texto}')
	finalText = ''
	for letra in texto:
		ascii = ord(letra)
		ascii-=1
		finalText += chr(ascii)
	return finalText

def encriptarArchivo(route):
	archivo = open(route, 'r')
	texto = archivo.read()
	archivo.close()
	textoEncriptado = encriptar(texto)

	archivo = open(route, 'w')
	archivo.write(textoEncriptado)
	archivo.close()
	print(f'Texto encriptado: {textoEncriptado}')

def desencriptarArchivo(route):
	archivo = open(route, 'r')
	texto = archivo.read()
	archivo.close()
	textoDesencriptado = desencriptar(texto)

	archivo = open(route, 'w')
	archivo.write(textoDesencriptado)
	archivo.close()
	print(f'Texto desencriptado: {textoDesencriptado}')

route = input("Enter the file's route: > ")
conf = input('1-Encriptar o 2-Desencriptar: > ')
while(conf=='1' or conf=='2'):
	if conf == '1':
		encriptarArchivo(route)
	elif conf == '2':
		desencriptarArchivo(route)
	conf = input('1-Encriptar o 2-Desencriptar: > ')
