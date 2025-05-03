function mergeSortedArrays(arr1, arr2){
    arr3 = arr1.concat(arr2);
    for (let i=0; i < arr3.length; i++){
       if(arr3[i] > arr3[i+1]){
        arr = arr3[i+1];
        arr3[i+1] = arr3[i];
        arr3[i] = arr;
       }
    }
}

mergeSortedArrays([0,3,4,31], [4,6,30])