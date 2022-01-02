// C program to implement recursive Binary Search
#include <stdio.h>
#include<stdlib.h>

// A recursive binary search function. It returns
// location of x in given array arr[l..r] is present,
// otherwise -1
int binarySearch(int arr[], int l, int r, int x)
{
	if (r >= l) {
		int mid = l + (r - l) / 2;

		// If the element is present at the middle
		// itself
		if (arr[mid] == x)
			return mid;

		// If element is smaller than mid, then
		// it can only be present in left subarray
		if (arr[mid] > x)
			return binarySearch(arr, l, mid - 1, x);

		// Else the element can only be present
		// in right subarray
		return binarySearch(arr, mid + 1, r, x);
	}

	// We reach here when element is not
	// present in array
	return -1;
}

int compare(const void* a, const void* b)
{
	int int_a = *((int*)a);
	int int_b = *((int*)b);

	if (int_a == int_b) return 0;
	else if (int_a < int_b) return -1;
	else return 1;
}

int main(void)
{
	int number = 100, random=0,jj=0,gg=0;
	int arr[100],duplicate[50],key[50];
	int n = sizeof(arr) /sizeof( arr[0]);

	/*printf("Enter Count Number : ");
	scanf_s("%d", &number);*/
	for (int i = 0; i < number; i++)
	{
		random = rand() % 100;
		
		printf("%d random number : %d\n", i, random);
		qsort(arr, n, sizeof(int), compare);		
		int result = binarySearch(arr, 0, n - 1, random);
		if (result == -1)
		{
			arr[jj] = random;
			jj++;
		}
		else {
			key[gg] = random;
			gg++;
			//printf("Element is present at index %d", result);
		}
	}

	printf("\nsorting arr : ");
	for (int a = 0; a < n; a++) {
		if (arr[a] >= 0) {
			printf("%d ", arr[a]);
		}
		
	}
	printf("\n");

	printf("\nFinding Key arr : ");
	for (int a = 0; a < n; a++) {
		if (key[a] >= 0) {
			printf("%d ", key[a]);
		}	
	}
	printf("\n");	
	

	/*int x = 16;
	int result = binarySearch(arr, 0, n - 1, x);
	(result == -1)
		? printf("Element is not present in array")
		: printf("Element is present at index %d", result);*/
	return 0;
}
