class Fibonacci:
	"""docstring num, terms fibonacci"""
	def __init__(self, num, terms):
		#super(fibonacci, self).__init__()
		self.num = num
		self.terms = terms

	def fibonacci_upto_a_number(self):
		num1 = 0
		num2 = 1
		num3 = 0
		series_num = [0, 1]
		while num3 < self.num:
			num3 = num1 + num2
			num1, num2 = num2, num1+num2
			if num3 < self.num:
				series_num.append(num3)
			else:
				break
		return series_num

	def fibonacci_upto_N_terms(self):
		num1 = 0
		num2 = 1
		num3 = 0
		series_num = [0, 1]
		for i in range(0,self.terms-2):
			num3 = num1 + num2
			num1, num2 = num2, num1+num2
			series_num.append(num3)
		return series_num


ask = input('What kind of series do you want to generate?Upto a Number(N) or upto N terms(T)?\nPress N or T: ')
while True:
	if ask.lower() == 'n':
		print('Please enter a Number:')
		number = input()
		try:
			series1 = Fibonacci(int(number), 1)
			print(series1.fibonacci_upto_a_number())
			break
		except:
			print('Sorry, wrong input! Input must be an integer.')
			continue

	elif ask.lower() == 't':
		print('Please enter number of terms:')
		term = input()
		try:
			series2 = Fibonacci(1, int(term))
			print(series2.fibonacci_upto_N_terms())
			break
		except:
			print('Sorry, wrong input! Input must be an integer.')
			continue

	else:
		print('Sorry! wrong input.')
		break
