# From codewars: take DNA string and swap it.
def DNA_strand(dna):
	opposites = {"A":"T", "T":"A", "C":"G", "G":"C"}
	newWord = ""
	for letter in dna:
		newWord = newWord + opposites[letter]
	return newWord

# Since that one took a few minutes, I did the next "kata" which was an interest-rate problem. Solved by:
def calculate_years(principal, interest, tax, desired):
    years = 0
    
    while principal < desired:
        principal += (interest * principal) * (1 - tax)
        years += 1
        
    return years
  
# unlocked new KYU!!! I also just started working with react.
