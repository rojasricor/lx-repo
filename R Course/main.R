x <- -3

print("The video is paused in 01:32:12")

if (x < 0) {
	print("x es un numero negativo")
}

x <- 5

if (x < 0) {
	print("x es un numero negativo")
} else if (x == 0) {
	print("x es un cero")
} else {
	print("x es un numero positivo")
}

ifelse(x > 0, "Is positive", "Is negative")

x <- "red"
switch(x, red="cloth", size=6, name="Table")
