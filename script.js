function calculate() {
    //Creating Array
    var string = document.getElementById("numbers").value;
    var array = string.split(" ")
    for(var x=0; x < array.length; x++) { array[x] = +array[x]; }

    
    //Mean
    var sum = 0;
    for(var x=0; x < array.length; x++) { sum = sum + array[x]; }
    console.log(sum);
    var mean = sum / array.length;
    
    //Median
    var median = 0;
      if (array.length % 2 === 0) { //Even
          median = (array[array.length / 2 - 1] + array[array.length / 2]) / 2;
      } else { //Odd
          median = array[(array.length - 1) / 2];
      }
    
    //Mode
    var mode = [];
    for(x=0; x < array.length; x++) {if(array[x] === array[x + 1]) {
      mode.push(array[x]);
    }}
    
    let result = document.getElementById("result");
    result.innerHTML = "<br> <br><h2>Results</h2> <br>" + "<p>Mean</p>" + mean + "<br><br><p>Median</p>" + median
    + "<br><br><p>Mode</p>" + mode;
    }
  
  document.getElementById("numbers").value = "";