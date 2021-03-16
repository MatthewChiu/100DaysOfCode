# Started the day learning more react — having fun with it. 
# Realized that I need more js to grasp it better.

# Did code wars for JS: Square individual elements for list of numbers and concatenate into a single number.
function squareDigits(input){
  let output = []
  for (i of String(input)){
    let tempNumber = i * i
    output.push(String(tempNumber))
  }
  console.log(Number(output.join('')))
#   Or return... Number(output.join(''))
}

squareDigits(256)
