def get_sum(a,b):
	number = 0
	if a == b:
		number = a
	if a < b:
		for i in range(a,b+1):
			number+=i
	if b < a:
		for i in range(b, a+1):
			number +=i
	return number




get_sum(0, -1)