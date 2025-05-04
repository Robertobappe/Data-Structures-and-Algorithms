//Google Question
//Given an array = [2,5,1,2,3,5,1,2,4]:
//It should return 2

//Given an array = [2,1,1,2,3,5,1,2,4]:
//It should return 1

//Given an array = [2,3,4,5]:
//It should return undefined

//Brute force
function firstRecurringCharacter(arr){
    for(let i=0; i< arr.length;i++){
        for(let j=i+1; j< arr.length;j++){
            if(arr[i] === arr[j]){
                return arr[i];
            }
        }
    }
    return undefined;
} //O(n^2)
//O(1)

//Better solution
function firstRecurringCharacter2(arr){
    let map = {}; //O(n)
    for(let i=0; i<arr.length; i++){
        if(map[arr[i]]){
            return arr[i];
        }
        map[arr[i]] = true;        
    }
    return undefined;    
}//O(n)

console.log(firstRecurringCharacter([2,5,1,2,3,5,1,2,4]));
//brute force doesn't work for [2,5,5,2,3,5,1,2,4]