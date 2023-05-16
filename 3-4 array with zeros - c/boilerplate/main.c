/*
	Date: 1/30/2023
	Assignment: Leetcode #121 best time to buy and sell stocks
	Description: sliding glass approach to find the biggest profit
*/
#include "header.h"

#define SIZE 50

void fillIntArray(int* array) { // ask for a pointer to the start of the array
	srand((unsigned int)time(NULL));

	printf("Array: ");
	// generate array with zeros
	for (int i = 0; i < SIZE; i++) {
		array[i] = rand() % 5; // 0 - 4
		if (i != SIZE - 1) printf("%d,", array[i]);
		else printf("%d", array[i]);
	}
}

int main(void) {
	int array[SIZE];

	// generate a random array of integers
	fillIntArray(array);

	// start with a pointer to the start of the array and the end
	int left = 0, right = SIZE - 1;
	
	// traverse the array
	while (left < right) {
		while (array[right] == 0) right--; // skip any zeros at the right because theyre already in place
		// now we know right points to a non zero, so get to the first left zero
		while (array[left] != 0) left++;
		// swap left value and right value. Unless left has eclipsed right
		if (left < right) {
			int temp = array[left];
			array[left] = array[right];
			array[right] = temp;
		}
		// print each step
		printf("\nArray: ");
		for (int i = 0; i < SIZE; i++) {
			if (i != SIZE - 1) printf("%d,", array[i]);
			else printf("%d", array[i]);
		}
	}

	// print the result
	printf("\nResult: ");
	for (int i = 0; i < SIZE; i++) {
		if (i != SIZE - 1) printf("%d,", array[i]);
		else printf("%d", array[i]);
	}

	printf("\n\n\n");
	return 0;
}