//Given 2 arrays, create a function that let's a user know (true/false)
//whether these two arrays contain any comomom items
//For example:
//const array1 = ['a','b','c','x'];
//const array2 = ['z','y','i'];
//should return false
//-------------------------------------------------------------------
const array1 = ['a','b','c','x'];
const array2 = ['z','y','x'];
//should return true

//2 parameters - arrays - no size limit
//return true or false

//not a better solution - brute force --> O(a*b) Time complexity
//O(1) - Space complexity
function containsCommonItem(arr1,arr2){
    for(let i=0; i<arr1.length;i++){
        for(let j=0; j<arr2.length;j++){
            if(arr1[i] == arr2[j]){
                return true;
            }
        }
    }
    return false;
}

//retorno = containsCommonItem(array1,array2);
//console.log(retorno);

//-------------------------------------------------------------------
// let's create a hase table or in javascript called object
// array1 ==> obj{
// a: true,
// b: true,
// c: true,
// x: true
//}
// array2[index] === obj.properties

//O(a+b) - Time complexity
//O(a) - Space complexity
function containsCommonItem2(arr1,arr2){
    //loop through first array and create object where properties === items inte array
    //note: we can modularized this part of the code --> function to transfor into a map
    let map = {};
    for(let i=0; i<arr1.length;i++){
        if(!map[arr1[i]]){
            const item = arr1[i];
            map[item] = true;
        }
    }
    //loop through second array and check if item in second array exists on created object
    for(let j=0; j<arr2.length; j++){
        if(map[arr2[j]]){
            return true;
        }
    }
    return false;
}

a=containsCommonItem2(array1,array2);
console.log(a);