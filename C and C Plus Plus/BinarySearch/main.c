#include <stdio.h>


int BinarySearch(int arr[],int init,int length,int search);

int main() {
    int data[5] = {10,20,30,40,50};
    int search=50;
    int length = sizeof (data)/sizeof (data[0]);
    int result =BinarySearch(data,0,length,search);
    if(result!=-1){
        printf("%d found at index %d",search,result );
    } else{
        printf("Element not found");
    }

    return 0;
}

int BinarySearch(int arr[],int init,int length,int search){
    if(length>= init){
      int mid = length - (length-init)/2;
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