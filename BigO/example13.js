//[1,2,3,9] sum=8 --> no
//[1,2,4,4] sum=8 --> yes
//you can't repeat the same element at the same index twice
//but certainly the same number may apper twice
//the numbers are integers and negatives cloud happen

//simplest solution
//O(n^2) - Time complexity
//O(1) - Space complexity
arr1 = [1,2,3,9];
arr2 = [1,2,4,4];
sum=8;

function sumPar(arr,sum){
    for(let i=0; i<arr.length-1;i++){
        for(let j=i+1; j<arr.length; j++){
            if(arr[i] + arr[j] === sum){
                return true;
            }
        }
    }
    return false;
}

//----------------------------------------------------------
arr1 = [1,2,3,9];
arr2 = [1,2,4,4];
sum=8;

function sumPar2(arr,sum){
    map = {};
    for(let i=0; i<arr.length;i++){
        if(!map[arr[i]]){
            map[arr[i]] = true;
        }
    }
    for(let j=0; j<arr.length; j++){
        let sub = sum -arr[j];
        if(map[sub]){
            return true;
        }
    }
    return false;
}

//--------------------------------------------------------------------
//if the array is sorted
//binary search
arr1 = [1,2,3,9];
arr2 = [1,2,4,4];
sum=8;

function sumPar3(arr,sum){
    let i = 0;
    let j = arr.length - 1;
    let sum_=0;
    while(i < j){
        sum_ = arr[i] + arr[j];
        if(sum_ === sum){
            return true;
        }
        if(sum_<sum){
            i++;        
        }
        if(sum_>sum){
            j--;
        }
    }
    return false;
}

//console.log(sumPar3(arr2,sum));

//--------------------------------------------------------------------
//great solution
arr1 = [1,2,3,9];
arr2 = [1,2,4,4];
sum=8;

function sumPar4(arr,sum){
    const myset = new Set();
    const len = arr.length;

    for(let i=0; i<len; i++){
        if(myset.has(arr[i])){
            return true;
        }
        myset.add(sum - arr[i]);
    }
    return false;
}

console.log(sumPar4(arr2,sum));