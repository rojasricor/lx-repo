#include "stdio.h"
#define PI 3.1416

double GradestoRadians(double Grades) {
	return Grades * PI / 180;
}

double RadianstoGrades(double Radians) {
	return Radians * 180 / PI;
}

int main() {
	printf("Converting grades to radians: \n");
	double Grades;
	printf("Enter the number of Grades to convert to Radians: \n");
	scanf("%lf", &Grades);
	double newRadians = GradestoRadians(Grades);
	printf("%.4f Grades to Radians are %.4f Radians.\n", Grades, newRadians);
	printf("\n\n");

	printf("Converting grades to radians: \n");
	double Radians;
	printf("Enter the number of Radians to convert to Grades: \n");
	scanf("%lf", &Radians);
	double newGrades = RadianstoGrades(Radians);
	printf("%.4f Radians to Grades are %.4f Grades.\n", Radians, newGrades);
	return 0;
}
