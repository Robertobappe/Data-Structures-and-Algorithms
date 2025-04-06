const nemo = ['nemo'];
const everyone = ['dory', 'bruce', 'marlin', 'gill', 'bloat', 
    'nigel', 'squirt', 'darla', 'hank','nemo'];
    //Rule 1: worst case

function findNemo1(array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('Found NEMO!');
    }
  }
}

findNemo1(everyone);