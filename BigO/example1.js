const nemo = ['nemo']; //O(1)
const everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank'];
const large = new Array(10000).fill('nemo'); //O(10000)

function findNemo1(array) {
  let t0 = performance.now();
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('Found NEMO!');
    }
  }
  let t = performance.now();
  console.log('Call to find Nemo took ' + (t-t0) + ' milliseconds');
}

findNemo1(large); //O(n) --> Linear Time