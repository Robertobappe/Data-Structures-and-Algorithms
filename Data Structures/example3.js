//Create a function that reverses a string:
//'Hi My name is Andrei' should be:
//'ierdnA si eman yM iH'

//My own solution
function reverses(str){
    arr = str.slice(); //a string is a array when acessed like str[i]
    arrReverse = [];
    strReverse = '';

    for(let i=0; i < str.length; i++){
        arrReverse[str.length - i -1] = arr[i];
    }
    for(let j=0; j < str.length; j++){
        strReverse += arrReverse[j];
    }
    return strReverse;
}
console.log(reverses('Hi My name is Andrei'));

//Instructor solution
function reverse(str){
    if(!str || typeof str != 'string' || str.length < 2 ) return str;
    
    const backwards = [];
    const totalItems = str.length - 1;
    for(let i = totalItems; i >= 0; i--){
      backwards.push(str[i]);
    }
    return backwards.join('');
  }
  
  function reverse2(str){
    //check for valid input
    return str.split('').reverse().join('');
  }
  
  const reverse3 = str => [...str].reverse().join('');
  
  reverse('Timbits Hi')
  reverse('Timbits Hi')
  reverse3('Timbits Hi')
