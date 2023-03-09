#include "stdio.h"
#include "math.h"

double calcularDistancia(int x1, int y1, int x2, int y2) {
	return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

int main() {
	int x1 = 6, y1 = -3;
	int x2 = 56, y2 = -223;
	double distancia = calcularDistancia(x1, y1, x2, y2);
	printf("La distancia entre las coordenadas [%d,%d][%d,%d] = %1f\n", x1, y1, x2, y2, distancia);
	return 0;
}
