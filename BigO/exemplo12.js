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

//not a better solution - brute force --> O(a*b)
function containsCommonItem(arr1,arr2){
    for(let i=0; i<arr1.length;i++){
        for(let j=0; j<arr2.length;j++){
            if(arr1[i] == arr2[j]){
                return true;
            }
        }
    }
    return false;}

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

function containsCommonItem2(arr1,arr2){
    //loop through first array and create object where properties === items inte array
    //loop through second array and check if item in second array exists on created object
    //O(a+b)
}