#include "stdio.h"
#include "string.h"
#define MAX_LENGTH_CHAR 50

int otherExample() {
	char pornstar1[MAX_LENGTH_CHAR] = "Lana Rhoades";
	char pornstar2[MAX_LENGTH_CHAR] = "Mia Khalifa";
	char tijeras[MAX_LENGTH_CHAR];
	printf("Mi actriz porno favorita: %s, otra actriz porno favorita: %s\n", pornstar1, pornstar2);

	strncpy(tijeras, pornstar1, MAX_LENGTH_CHAR);
	strncpy(pornstar1, pornstar2, MAX_LENGTH_CHAR);
	strncpy(pornstar2, tijeras, MAX_LENGTH_CHAR);
	printf("Mi actriz porno favorita: %s, otra actriz porno favorita: %s\n", pornstar1, pornstar2);
	return 0;
}

int main(void /*this is optional*/) {
	char name[MAX_LENGTH_CHAR] = "Ricardo";
	char temporal[MAX_LENGTH_CHAR] = "";

	strncpy(temporal, name, 1);
	printf("Name: %s Temporal: %s\nUsing strncpy...\n", name, temporal);
	strcpy(temporal, name);
	printf("Name: %s Temporal: %s\nUsing strcpy...\n", name, temporal);

	printf("\n\n");

	return otherExample();
}