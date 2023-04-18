/*
	Date: 1/30/2023
	Assignment: Leetcode #121 best time to buy and sell stocks
	Description: sliding glass approach to find the biggest profit
*/
#include "header.h"

// Erick's solution. Just keep moving r, checking the profit each time, saving it if its a high, and only move l when a new low is discovered
int maxprof(int* arr, int arrlen) {
	int l = 0, prof = 0;
	for (int r = 1; r < arrlen; r++) {
		if (arr[l] < arr[r] && prof < (arr[r] - arr[l])) {
			prof = (arr[r] - arr[l]);
		}
		if (arr[r] < arr[l]) {
			l = r;
		}
	}
	return prof;
}

int main(void) {
	int arr[20] = { 7,1,11,-1,2,0,0,0,10,-4,5,3,63,5,-7,52,4535,6,6 };
	int arrLen = sizeof(arr) / sizeof(arr[0]);
	int l = 0, r = 1, rmax = 0, profit = 0, maxProf = 0, exitloop = 0;
	while (r < arrLen - 1) {
		exitloop = 0;

		// these first 2 moves are when you know the profit will be bigger. were starting at 1 - 7 = -6, so if the next r (3) is higher 
		// than 1 we get 3 - 7 = -4. if the next l (1) is lower than 7 we get 3 - 1 = 2. These are the freebie cases.
		if (arr[r + 1] >= arr[r]) r++, rmax = arr[r];
		else if (arr[l + 1] <= arr[l] && l < r - 1) l++;
		// once we run out of freebie cases, we start moving r until either we find a new min OR a new max. so we find -1 and set l to that. then right goes to 2 
		// by the freebie cases and we get 2 - -1 = 3. eventually right gets to 10 and we get 10 - -1 = 11. then right goes to 4, max profit remains, 
		// we know theres no number lower than -1 or higher than 10 occuring after -1 and were done
		else {
			while (r < arrLen - 1 && exitloop == 0) {
				// check profit
				profit = rmax - arr[l];
				if (profit > maxProf) maxProf = profit;
				printf("left: %d, right: %d, prof: %d, maxProf: %d\n", l, r, profit, maxProf);

				r++;
				if (arr[r] >= rmax) rmax = arr[r], exitloop = 1;
				if (arr[r] <= arr[l]) l = r, rmax = 0, exitloop = 1; // when we jump l to r at a new min, we need to invalidate rmax since its now behind l and unusable

				// check profit
				profit = rmax - arr[l];
				if (profit > maxProf) maxProf = profit;
			}
		}
		printf("left: %d, right: %d, prof: %d, maxProf: %d\n", l, r, profit, maxProf);
	}
	
	//maxProf = maxprof(arr, arrLen);

	printf("max Profit = %d\n", maxProf);

	printf("\n\n\n");
	return 0;
}