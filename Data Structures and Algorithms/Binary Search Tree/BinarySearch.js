function binarySearch(arr, l, r, x) {
    if (r >= l) {
        let mid = l + Math.floor((r - l) / 2);
        // console.log("mid : "+mid)
        if (arr[mid] == x) {
            return mid
        }
        if (arr[mid] > x) {
            return binarySearch(arr,l,mid-1,x)
        }
        return binarySearch(arr,mid+1,r,x)
    }
    return -1;
}

let arr = [1, 2, 3, 5,40]
let x = 40
let n = arr.length
let result = binarySearch(arr, 0, n - 1, x);
// console.log("result : " + result);

if (result != -1) {
    console.log("Element is present at index " + result);
} else {    
    console.log( "Element is not present in array")
}

