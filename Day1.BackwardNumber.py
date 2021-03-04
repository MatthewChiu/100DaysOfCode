def descending_order(num):
    # Bust a move right here
    newNum = []
    for number in str(num):
    	newNum.append(int(number))

    reverseNumber = []
    for index, number in enumerate(sorted(newNum)):
    	reverseNumber.insert(0, number)
    newReverseNumber = ""

    for number in reverseNumber:
    	newReverseNumber = newReverseNumber + str(number)
    return int(newReverseNumber)

descending_order(2878)