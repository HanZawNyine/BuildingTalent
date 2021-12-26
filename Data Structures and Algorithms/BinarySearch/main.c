#include <stdio.h>
#include <stdlib.h>

int BinarySearch(int arr[],int init,int length,int search);
int * ReadingFile(char fileName[]);

int  *sorting(int arr[],int length);


int main() {

    int *unSortData;
    int ToSortData[10];

    unSortData = ReadingFile("../file.txt");
        int i=0;
        while (*(unSortData+i) != 0){
//            printf("%d, %d\n",i,*(unSortData+i));
            ToSortData[i]=*(unSortData+i);
//            printf("%d\n",ToSortData[i]);
            i++;
        }

//
//    int zzz=0;
//    while (ToSortData[zzz]!= 0){
//        //printf("%d\n",ToSortData[zzz]);
//        zzz++;
//    }

    //Calculate length of array arr
    int length = sizeof(ToSortData)/sizeof(ToSortData[0]);
    int *soterdData = sorting(ToSortData,length);
    soterdData = sorting(ToSortData,length);

    int jj=0,sorter[10];
    printf("Original Array : ");
    while (jj!=10){
        sorter[jj]=soterdData[jj];
        printf("%d ",sorter[jj]);
        jj++;
    }
    printf("\n");
//    selectionSort(ToSortData, n);
//    printf("\nSorted array in Ascending order: \n");
//    printArray(ToSortData, n);


//    int data[5] = {10,20,30,40,50};
    int search=40;
    length = sizeof (sorter)/sizeof (sorter[0]);
    int result =BinarySearch(sorter,0,length,search);
    if(result!=-1){
        printf("%d found at index %d",search,result );
    } else{
        printf("Element not found");
    }

    return 0;
}

int BinarySearch(int arr[],int init,int length,int search){
    if(length>= init){
      int mid = length- (length-init)/2;
      if(arr[mid]==search){
          return mid;
      }
      if(arr[mid]>search){
          return BinarySearch(arr,init,mid-1,search);
      }

      return BinarySearch(arr,mid+1,length,search);
    }
    return -1;
}

int * ReadingFile(char fileName[]) {
//    int data[50];
    static int  data[100];
    FILE *filePointer;
    int bufferLength = 255;
    char buffer[bufferLength];

    filePointer = fopen(fileName, "r");
    if (filePointer != NULL) {
        int i = 0;
        while (fgets(buffer, bufferLength, filePointer)) {
            data[i] = atoi(buffer);
//            printf("%d\n", data[i]);
            i++;
        }
        fclose(filePointer);
        return  data;
    }
    return data;
}

int  *sorting(int arr[],int length){
    int temp = 0,sorted[10];
    //Displaying elements of original array
//    printf("Elements of original array: \n");
//    for (int i = 0; i < length; i++) {
//        printf("%d ", arr[i]);
//    }

    //Sort the array in ascending order
    for (int i = 0; i < length; i++) {
        for (int j = i+1; j < length; j++) {
            if(arr[i] > arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    return  arr;
}