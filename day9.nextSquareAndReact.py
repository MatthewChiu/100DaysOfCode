# Started the coding day with some react, but then moved to codwars to do an exercise in JS: find the next square after a given one. Otherwise return -1.

function findNextSquare(sq) {
    let squareNum = Math.sqrt(sq) 
    if (Number.isInteger(squareNum)) {
        nextNum = (squareNum+1)*(squareNum+1)
        return nextNum
    } else {
        return -1
    }
  }
