ctr <- 1

while(ctr <= 7) {
	print(paste("ctr vale", ctr))
	ctr <- ctr + 1
}

ctr <- 1

while(ctr <= 7) {
	if (ctr%%5 == 0)
		break
	print(paste("ctr vale", ctr))
	ctr <- ctr + 1
}

cities <- c("New York", "Paris", "London", "Tokyo", "Cape Town", "Peak")
for(city in cities)
	print(city)

cities <- c("New York", "Paris", "London", "Tokyo", "Cape Town", "Peak")
for(city in cities) {
	if(nchar(city) == 0)
		next
	print(city)
}

cities <- c("New York", "Paris", "London", "Tokyo", "Cape Town", "Peak")
for(i in 1:length(cities))
	print(paste(cities[i], "esta en la posicion", i, "del vector de ciudades"))
